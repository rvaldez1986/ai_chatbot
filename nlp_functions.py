# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 20:53:27 2019

@author: rober
"""

import numpy as np
from nltk.tokenize import RegexpTokenizer
from nltk.stem import SnowballStemmer
import unidecode
from textblob import TextBlob
import wikipedia
import re
from pattern.es import parse, parsetree
import requests
import smtplib
import json
import nltk


from urls import u_IESS, u_RDD, u_JP, u_CONS






tokenizer = RegexpTokenizer(r'\w+')
stemmer = SnowballStemmer("spanish")
base_url= "http://192.168.1.15:8080/actuaria-business/api"

def trim_sent(sentence):    
    return ' '.join(sentence.split())


def top_likelihood(t_dict, sentence):
    lik = -1
    tokens = tokenizer.tokenize(unidecode.unidecode(sentence.lower()))
    for w in tokens:
        w = stemmer.stem(w)
        if w in t_dict:
            #print(w)
            if lik == -1:
                if t_dict[w] == 0:
                    lik = -1
                else:
                    lik = t_dict[w]
            else:
                if t_dict[w] == 0:
                    lik -= 1
                else:
                    lik += t_dict[w]
    return lik


def percent_greet(sentence):
    tgreet = ['hol', 'buen', 'tard', 'dias', 'noch']
    count = 0
    tokens = tokenizer.tokenize(unidecode.unidecode(sentence.lower()))
    for w in tokens:
        w = stemmer.stem(w)
        if w in tgreet:
            count += 1            
    return count/len(tokens) 


def polarity(message): #blob has a limit on api calls
    blob = TextBlob(message)
            
    if blob.detect_language() != 'en':
        blob = blob.translate(to='en').lower() 
    else:
        blob = blob.lower()            
            
    pol = blob.sentiment[0]
    return pol

def n_token(sentence):
    tokens = tokenizer.tokenize(unidecode.unidecode(sentence.lower()))       
    return len(tokens) 

def y_hat(p_greet, pol, max_topic):
    options = {-1: "na", 0: "Jubilacion Patronal", 1: "Renuncia/Despido/Desahucio", 
                   2: "IESS", 3: "Contacto", 4: "Otros servicios (Charlas/Capacitaciones/Financiera)", 
                       5: "Consultoria", 6: "job seeker"}    
    if pol<0 and max_topic == -1:
        ret = "Queja"
    elif pol <= -0.45:
        ret = "Queja"
    elif p_greet>= 0.5:
        ret = "Greeting"
    elif max_topic == -1 and pol >= 0.9:
        ret = "Hi Five"
    else:
        ret = options[max_topic]
    return ret


def predict_topic(sentence):
    jbtopdict = np.load('Data\\jbtopdict.npy', allow_pickle=True).item()
    rentopdict = np.load('Data\\rentopdict.npy', allow_pickle=True).item()
    IESStopdict = np.load('Data\\IESStopdict.npy', allow_pickle=True).item()
    CONTtopdict = np.load('Data\\CONTtopdict.npy', allow_pickle=True).item()
    OStopdict = np.load('Data\\OStopdict.npy', allow_pickle=True).item()
    CONStopdict = np.load('Data\\CONStopdict.npy', allow_pickle=True).item()
    JStopdic = np.load('Data\\JStopdict.npy', allow_pickle=True).item()  
    
    sentence = trim_sent(sentence)
    
    jp = top_likelihood(jbtopdict, sentence)
    ren = top_likelihood(rentopdict, sentence) 
    iss = top_likelihood(IESStopdict, sentence) 
    ct = top_likelihood(CONTtopdict, sentence) 
    osl = top_likelihood(OStopdict, sentence) 
    cons = top_likelihood(CONStopdict, sentence) 
    js = top_likelihood(JStopdic, sentence)
    
    p_greet = percent_greet(sentence) 
    pol = polarity(sentence)
    
    topic_l = np.array([jp,ren,iss,ct,osl,cons,js])
    t  = np.argmax(topic_l)
    v = topic_l[t]
    max_topic = t if v>=0 else -1
    
    yhat = y_hat(p_greet, pol, max_topic) 
    
    return (yhat, pol, sentence)



def proc_wiki(message):
    try:
        wikipedia.set_lang('es')
        ans = wikipedia.summary(message, sentences=0, chars=500, auto_suggest=True, redirect=True)
        ans = str(ans)
        ans = 'Lo que sé de este tema es: ' + ans
    except:
        ans = 'No se mucho de este tema'
    
    return ans    
    
    
def proc_message1ST(message):
    try:
        message = message.lower()
        
        p1 = message.find('persona')
        p2 = message.find('empresa')
        
        if p1 != -1 and p2 == -1:
            ans = 'persona'
        elif p1 == -1 and p2 != -1:
            ans = 'empresa'
        else:
            ans = 'na'
    except:
        ans = 'na'
        
    return ans
    
    
def proc_messageYN(message):
    try:
        message = message.lower()
        
        p1 = message.find('si')
        p2 = message.find('no')
        
        if p1 != -1 and p2 == -1:
            ans = 'si'
        elif p1 == -1 and p2 != -1:
            ans = 'no'
        else:
            ans = 'na'
    except:
        ans = 'na'
        
    return ans


def proc_message1NT(message):
    try:
        message = message.lower()
        
        p1 = message.find('actuaria')
        p2 = message.find('otro')
        
        if p1 != -1 and p2 == -1:
            ans = 'actuaria'
        elif p1 == -1 and p2 != -1:
            ans = 'otro'
        else:
            ans = 'na'
    except:
        ans = 'na'
        
    return ans


def proc_message2ST(message):
    try:
        ind = 0
        nlist = [s for s in re.findall(r'\b\d+\b',message)]
        ruc=None 
        for n in nlist:
            if val_RUC(n):
                ind += 1
                ruc=n
        if ind == 1:
            ans = ruc
        else:
            ans = 'na'
    except:
        ans = 'na'
    return ans


def val_RUC(string):
    if len(string) == 13:  #por ahora solo chequea el length
        return True
    else:
        return False


        
def proc_message_pro(message):
    try:
        ind = 0
        nlist = [s for s in re.findall(r'\b\d+\b',message)]
        np = None
        for n in nlist:
            if val_Proc(n):
                ind += 1
                np = n
        if ind == 1:
            ans = np       
        else:
            ans = 'na'
    except:
        ans = 'na'
    return ans

def val_Proc(string):
    if len(string) == 5:  #por ahora solo chequea el length
        return True
    else:
        return False   



def azure_q1(message):
    headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': '55c4f6fd25a84e81bc2369845f18f9bf',
    }

    params ={
            # Query parameter
            'q': message,
            # Optional request parameters, set to default values
            'timezoneOffset': '-360',
            'verbose': 'true',
            'spellCheck': 'false',
            'staging': 'false',
    }


    try:
        r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/d8bd8e1e-7a79-4a00-aa99-4fbc8b1a8425',headers=headers, params=params)
        payload = r.json()
        #intents = payload['intents']  #en prox modelo se puede trabajar con probabilidades de intents, por ahora solo pasa max
        entities = payload['entities']
        topIntent = payload['topScoringIntent']['intent']
        return (topIntent,entities)        

    except Exception as p:
        return ('None',None)
        print(p)
        
 
        
    

def position(l, b, element):
    try:
        p = l[b:].index(element)
        return p
    except:
        return -1


def cmin(*args):
    a = np.array(list(args))
    a = a[a>=0]
    if len(a)>0:
        return np.min(a)
    else:
        return -1
    
    
def ext_algo1(sentence):  
    words = []
    
    for s in parse(sentence.lower(), lemmata = True).split():        
   
        tags = [x[1] for x in s]
        b = 0
        
        while b < len(tags) - 1:  
            w_g = []
            p = position(tags,b,'VB')
            if p == -1:
                break
            else:        
                w_g.append(s[b+p][4])
                b = b + p + 1
                while True:
                    p1 = position(tags,b,'VB')
                    p2 = position(tags,b,'NN')
                    p3 = position(tags,b,'NNS')
                    pm = cmin(p1,p2,p3)
            
                    if pm == -1:
                        b = len(tags)
                        break            
                    elif p1 == pm:
                        w_g.append(s[b+p1][4])#global pos
                        b = b + p1 + 1
                    elif p2 == pm:
                        w_g.append(s[b+p2][4])
                        b = b + p2 + 1
                        break
                    else:
                        w_g.append(s[b+p3][4])
                        b = b + p3 + 1
                        break                 
                words.append(w_g)
        
    return words   


def ext_algo2(sentence):  
    words = []
    
    for s in parse(sentence.lower(), lemmata = True).split():        
   
        tags = [x[1] for x in s]
        b = 0
        
        while b < len(tags) - 1:  
            w_g = []
            p_1 = position(tags,b,'WP$')
            p_2 = position(tags,b,'IN')
            p = cmin(p_1,p_2)            
            if p == -1:
                break
            else:        
                w_g.append(s[b+p][4])
                b = b + p + 1
                while True:
                    p1 = position(tags,b,'VB')
                    p2 = position(tags,b,'NN')
                    p3 = position(tags,b,'NNS')
                    pm = cmin(p1,p2,p3)
            
                    if pm == -1:
                        b = len(tags)
                        break            
                    elif p1 == pm:
                        w_g.append(s[b+p1][4])#global pos
                        b = b + p1 + 1
                    elif p2 == pm:
                        w_g.append(s[b+p2][4])
                        b = b + p2 + 1
                        break
                    else:
                        w_g.append(s[b+p3][4])
                        b = b + p3 + 1
                        break                 
                words.append(w_g)
        
    return words   


def class_palabra(lista):
    tokens = ['costo',  'cotización', 'cotizar',  'cotizacion',  'precio']
    r = 0
    for l in lista:
        if len(l)>0:
            for w in l:
                if w in tokens:            
                    r = 1
                    
    tokens2 = ['necesitar','requerir','actualizar']
    tokens3 = ['estudio', 'servicio']
    
    for l in lista:
        if len(l) == 2:
            if l[0] in tokens2 and l[1] in tokens3:
                r =1                    
        
    return r

def algo_clasificador(sentence):
    lista1 = ext_algo1(sentence)
    lista2 = ext_algo2(sentence)
    lista = lista1 + lista2
    r = class_palabra(lista)
    if r == 1:
        return 'Cotizacion'
    else:
        return 'Otra Cosa'

    
def consulta_ruc(ruc):
   headers  = {"Accept": "application/json", "authorization":"eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJhY3R1YXJpYS1idXNpbmVzcyIsIm5hbWUiOiJwb3J0YWwifQ.n8_EF7R7EKayhwU3Eu7IfTdyAgGdFgfuoCa871aSJ7AY8Xu4AHyInOSik8IOjQag_vULNwdtJOcAKxqWv3ZQLg"}
   URL= base_url+"/clientes/consulta-por-ruc/"+str(ruc)
   
   try:
        r = requests.get(url=URL,headers=headers)
        payload = r.json()
        razonSocial = payload["respuesta"]["razonSocial"]
        codigo_cliente_ruc = payload["respuesta"]["codigoCliente"]
               
      
        return (razonSocial,codigo_cliente_ruc)

   except Exception as p:
       print(p) 
       return ('None') 


def consulta_proc(num_proc):
   headers  = {"Accept": "application/json", "authorization":"eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJhY3R1YXJpYS1idXNpbmVzcyIsIm5hbWUiOiJwb3J0YWwifQ.n8_EF7R7EKayhwU3Eu7IfTdyAgGdFgfuoCa871aSJ7AY8Xu4AHyInOSik8IOjQag_vULNwdtJOcAKxqWv3ZQLg"}
   URL= base_url+"/vendedores/datos/"+str(num_proc)
   URL2= base_url+"/procesos/estado-proceso/"+str(num_proc)
   URL3=base_url+"/procesos/consultar/"+str(num_proc)
   try:
        r = requests.get(url=URL,headers=headers)
        payload = r.json()
        nombre_encargado = payload["respuesta"]["nombre"]
        Extension_encargado = payload["respuesta"]["extension"]
        correo_electronico = payload["respuesta"]["email"]
        
        r2 = requests.get(url=URL2,headers=headers)
        payload2 = r2.json()
        estado_proceso = payload2["respuesta"]   
        
        r3 = requests.get(url=URL3,headers=headers)
        payload3 = r3.json()
        codigo_cliente_proc = payload3["respuesta"]["codigoCliente"] 
        
        return (nombre_encargado,Extension_encargado,correo_electronico,estado_proceso,codigo_cliente_proc)        

   except Exception:
        return ('None')
    
    
def send_email(text, toaddr):
    try:
        fromaddr = "roberto.valdez@actuaria.com.ec"        
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        #server.connect("smtp.gmail.com",465)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(fromaddr, "Actuaria2021")
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        
        ret = 'success'
        
    except:
        ret = 'error'
        
    return ret

def hasNumbers(string):
    return bool(re.search(r'\d', string))

def hasBC(string):
    i = string.find('/')
    return bool(i != -1)

def other_check(token):    
    b1 = not hasNumbers(token)
    b2 = not hasBC(token)
    return (b1 and b2)


def token_and_clean(texto):
    palabras_funcionales = nltk.corpus.stopwords.words("spanish")    
    tokens = nltk.word_tokenize(texto, "spanish")
    tokens_limpios=[]
    for token in tokens:        
        if token not in palabras_funcionales:
            if len(token) > 2 and token not in tokens_limpios:  #>2 helps in filtering out common
                if other_check(token):
                    tokens_limpios.append(token)
    return tokens_limpios

def stem_lemma(word):
    stemmer = SnowballStemmer('spanish')
    word = parsetree(word, lemmata=True)[0].lemmata[0]
    word = stemmer.stem(word) 
    return word



def get_score(q, u, td):
    dt = td[u][1]
    dt2 = td[u][2]    
    q_tokens =  token_and_clean(q.lower())
    puntaje = 0
    k = 1  #factor for header
    for t in q_tokens:  
        t = stem_lemma(t)
        if t in dt:
            puntaje += dt[t]
        if t in dt2:
            puntaje += dt[t] * k
        
    return puntaje  



def suggest_url(question, topic):    
    
    try:    
        texts_data = json.load(open("Data\\texts_data.txt"))        
        ranking = []
        
        
        if topic == "Jubilacion Patronal":
            ulist = u_JP            
        elif topic == "Renuncia/Despido/Desahucio":
            ulist = u_RDD 
        elif topic == "IESS":
            ulist = u_IESS
        else:
            ulist = u_CONS 
        
        for u in ulist:
            score = get_score(question, u, texts_data)
            ranking.append(score)
            
        if np.max(ranking) > 0:
            url_res = ulist[np.argmax(ranking)]
            return url_res
        else:
            return None           
        
    except:
        return None      
    





