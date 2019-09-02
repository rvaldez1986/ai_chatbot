# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 20:53:27 2019

@author: rober
"""

import numpy as np
from nltk.stem import SnowballStemmer
import unidecode
from textblob import TextBlob
import wikipedia
import re
from pattern.es import parsetree
import requests
import smtplib
import json
import nltk

from urls import u_IESS, u_RDD, u_JP, u_CONS, u_OS

stemmer = SnowballStemmer("spanish")
palabras_funcionales = nltk.corpus.stopwords.words("spanish")    
base_url= "http://192.168.1.15:8080/actuaria-business/api"



def trim_sent(sentence):    
    return ' '.join(sentence.split())


def prepare_text(text): 
    try:
        text = trim_sent(text).lower()
        return text
    except Exception as e:
        print('Exception en prepare_text: {0}'.format(e))
        return None       


def hasNumbers(string):
    return bool(re.search(r'\d', string))


def hasBC(string):
    i = string.find('/')
    return bool(i != -1)


def other_check(token):    
    b1 = not hasNumbers(token)
    b2 = not hasBC(token)
    return (b1 and b2)


def remove_accent(word):
    return unidecode.unidecode(word)


def stem_lemma(word):     
    word = parsetree(word, lemmata=True)[0].lemmata[0]
    word = stemmer.stem(word) 
    return word


def token_and_clean(texto): 
    tokens = nltk.word_tokenize(texto, "spanish")
    token_list = []
    for token in tokens:        
        if token not in palabras_funcionales:
            token = stem_lemma(token)
            token = remove_accent(token)
            if len(token) >= 2 and other_check(token):
                token_list.append(token)                
        
    return token_list   


def vectorize_phrase(texto, vocab):
    try:
        tokens = token_and_clean(texto)
        vector = np.zeros(len(vocab))
        for t in tokens:
            if t in vocab:
                vector[vocab.index(t)] = 1
        return vector
    
    except Exception as e:
        print('Exception en vectorize_phrase: {0}'.format(e))
        return None  
    

def n_token(sentence):
    token_list = token_and_clean(sentence) 
    return len(token_list) 


def polarity_and_lang(message): #blob has a limit on api calls
    
    try:
        if len(message) > 2:
    
            blob = TextBlob(message)    
        
            leng = blob.detect_language()
            text = ''
            if leng == 'es':
                blob = blob.translate(to='en').lower() 
                text = message
            else:
                blob = blob.lower() 
                text = blob.translate(to='es').lower().raw 
            
            pol = blob.sentiment[0]        
        else:
            print('Se paso a polarity_and_lang un texto menor que 3 caracters')
            pol = 0
            text = message            
            
        
    except Exception as e:
            print('Exception en polarity_and_lang: {0}'.format(e))
            pol = 0
            text = None            
    
    return (pol, text)


def percent_greet(sentence):
    tgreet = ['hol', 'buen', 'tard', 'dia', 'noch']
    count = 0
    tokens = token_and_clean(sentence)
    for w in tokens:       
        if w in tgreet:
            count += 1  
    if len(tokens) > 0:
        return count/len(tokens)
    else:
        return 0
    
def ex_capac(sentence):
    tcap = ['charl', 'curs', 'capacit', 'seminari', 'formacion', 'capacitacion']
    count = 0
    tokens = token_and_clean(sentence)
    for w in tokens:       
        if w in tcap:
            count += 1  
    return (count > 0)*1    


def pred_prob(text):
    try:        
    
        vocab = np.load('Data\\vocab.npy', allow_pickle=True)
        vocab = list(vocab)
    
        ldata = np.load('Data\\param_dict.npy', allow_pickle=True)
        param_dict = ldata.item() 
        W0 = param_dict[0].T
        b0 = param_dict[1]
        W1 = param_dict[2].T
        b1 = param_dict[3]
        
        pol, text = polarity_and_lang(text)
        
        if text:
    
            x = vectorize_phrase(text, vocab)
            if x.any():
                x = np.append(x, n_token(text))
                x = np.append(x, percent_greet(text))
                x = np.append(x, ex_capac(text))
                x = np.append(x, pol)   
    
                h0 = np.matmul(x, W0) + b0
                h1 = np.tanh(h0)
                h2 = np.matmul(h1, W1) + b1
                h3 = np.exp(h2)
                prob = h3/np.sum(h3)
                
                return (prob, pol, text)                
                    
            else:
                prob = np.zeros(13)
                prob[6] = 1  #probability of no topic is 100%
                return(prob, pol, text)
        
        else:
            return (np.zeros(13), pol, None)
    
    except Exception as e:
        print('Exception en predTop_prob: {0}'.format(e))
        return (np.zeros(13), None, None)
    
    
def predict_topic(sentence):
    topics = ['Jubilacion Patronal', 'Consultoria', 'Renuncia/Despido/Desahucio', 'IESS', 
                 'Greeting', 'Contacto', 'No Topic', 'Queja', 'Otros servicios', 'Charlas/Capacitaciones', 
                      'Hi Five', 'job seeker', 'Facturacion/Retencion/Cobros']    
    
    sentence = prepare_text(sentence)
    
    try:    
        if sentence:
            
            prob, pol, text = pred_prob(sentence)
            mprob = np.max(prob); scdprob = np.partition(prob, -2)[-2]
            t0 = topics[np.where(prob == mprob)[0][0]]; t1 = topics[np.where(prob == scdprob)[0][0]]
            
            if mprob > 0.625:
                return(t0, pol, text)
                
            elif mprob > 0.5: #unsure
                if t0 == 'No Topic' and t1 not in ['No Topic', 'Greeting', 'Hi Five']:
                    return ('U: NT: {0}'.format(t1), pol, text)
                
                elif scdprob > 0.3 and (t0 and t1) not in ['No Topic', 'Greeting', 'Hi Five']:
                    return('U: 2T: {0}, {1}'.format(t0, t1), pol, text)
                    
                elif t0 not in ['Greeting', 'Hi Five']:
                    return('U: 1T: {0}'.format(t0), pol, text)
                    
                else: #other possibilities
                    return ('U: NT: {0}'.format('Jubilacion Patronal'), pol, text)     
            
            else:
                return('U: NT: {0}'.format('Jubilacion Patronal'), 0, text) 
        
        else:
            return('U: NT: {0}'.format('Jubilacion Patronal'), 0, None) 
            
    except Exception as e:
        print('Exception en predict_topic: {0}'.format(e))
        return('U: NT: {0}'.format('Jubilacion Patronal'), 0, None)  
        
        
def assign_response0p5(ST, pred_topic, pol, OM, context, textos):
    
    if pred_topic in ST:
        ret_message = textos["ST"].format(pred_topic)
        context = [1, pred_topic, pol, OM, None, context[5]+1, None, None]      #Migra a estado 1
    
    elif pred_topic == "Queja":                                              
        ret_message = textos["Queja"]
        context = [1, pred_topic, pol, OM, None, context[5]+1, None, None]                
        
    elif pred_topic == "Hi Five":
        ret_message = textos["Hi Five"]
        context = [0, None, None, None, None, 0, None, None] 

    elif pred_topic == "job seeker":
        ret_message = textos["job seeker"]
        context = [0, None, None, None, None, 0, None, None]
        
    elif pred_topic == "Contacto":
        ret_message = textos["Contacto"]
        context = [0, None, None, None, None, 0, None, None]
        
    elif pred_topic == "Greeting":
        ret_message = textos["Greeting"]
        context = [0, None, None, None, None, 0, None, None]
        
    elif pred_topic == 'Charlas/Capacitaciones':
        ret_message = textos['Charlas/Capacitaciones']
        context = [0, None, None, None, None, 0, None, None]
        
    elif pred_topic == 'Facturacion/Retencion/Cobros':
        ret_message = textos['Facturacion/Retencion/Cobros']
        context = [0, None, None, None, None, 0, None, None]                 
    else:
        ret_message = textos['NT']           #No topic, could be wikipedia
        context = [1, 'NT', None, OM, None, context[5]+1, None, None]  
        
    return (ret_message, context)


    
    
def proc_messagep51(message, T0, T1):
    try:
        message = message.lower()
        
        p1 = message.find(T0)
        p2 = message.find(T1)
        p3 = message.find('ninguno')
        
        if p1 != -1:
            ans = T0
        elif p2 != -1:
            ans = T1
        elif p3 != -1:
            ans = 'NT'
        else:     
            ans = T0
    except Exception as e:
        print('Exception en proc_messagep50: {0}'.format(e))
        ans = T0
        
    return ans   
    
  


def proc_wiki(message):    
    try:
        wikipedia.set_lang('es')
        ans = wikipedia.summary(message, sentences=0, chars=500, auto_suggest=True, redirect=True)
        ans = str(ans)
        ans = 'Lo que sé de este tema es: ' + ans
    except Exception as e:
        print('Exception en proc_wiki: {0}'.format(e))
        ans = 'No se mucho de este tema'
    
    return ans    
    
    
def proc_message1ST(message):
    try:
        message = message.lower()        
        p1 = (message.find('persona') != -1) or (message.find('natural') != -1); p2 = (message.find('empresa') != -1)
        p3 = (message.find('salir') != -1)
        
        if p1 and not (p2 or p3):
            ans = 'persona'
        elif p2 and not (p1 or p3):
            ans = 'empresa'
        elif p3:
            ans = 'salir'
        else:
            ans = 'na'
    except Exception as e:
        print('Exception en proc_message1ST: {0}'.format(e))
        ans = 'na'
        
    return ans
    
    
def proc_messageYN(message):
    try:
        message = message.lower()
        
        p1 = (message.find('si') != -1); p2 = (message.find('no') != -1); p3 = (message.find('salir') != -1)
        
        if p1 and not (p2 or p3):
            ans = 'si'
        elif p2 and not (p1 or p3):
            ans = 'no'
        elif p3:
            ans = 'salir'
        else:
            ans = 'na'
    except Exception as e:
        print('Exception en proc_messageYN: {0}'.format(e))
        ans = 'na'
        
    return ans


def proc_message1NT(message):
    try:
        message = message.lower()
        p1 = (message.find('actuaria') != -1); p2 = (message.find('otro') != -1); p3 = (message.find('salir') != -1)    
        
        if p1 and not (p2 or p3):
            ans = 'actuaria'
        elif p2 and not (p1 or p3):
            ans = 'otro'
        elif p3:
            ans = 'salir'
        else:
            ans = 'na'
    except Exception as e:
        print('Exception en proc_message1NT: {0}'.format(e))
        ans = 'na'        
    return ans


def proc_message2ST(message):
    try:
        ind = 0
        nlist = [s for s in re.findall(r'\b\d+\b',message)]
        p3 = (message.find('salir') != -1)  
        ruc=None 
        for n in nlist:
            if val_RUC(n):
                ind += 1
                ruc=n
        if ind == 1:
            ans = ruc
        elif p3:
            ans = 'salir'
        else:
            ans = 'na'
    except Exception as e:
        print('Exception en proc_message2ST: {0}'.format(e))
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
   my_dict={"R":"Ingresado en Sistema","A":"Asignado a un tecnico","N":"En Desarrollo","D":"Esperando infromacion","L":"Finalizado por tecnico",
         "V":"Revisado","E":"Despachado","T":"Entregado al cliente","U":"Anulado","O":"Pagado y Entregado"} 
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
        
        return (nombre_encargado,Extension_encargado,correo_electronico,my_dict[estado_proceso.get(num_proc)],codigo_cliente_proc)        

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
        
    except Exception as e:
        print('Exception en send_email: {0}'.format(e))
        ret = 'error'
        
    return ret


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
        elif topic == "Consultoria":
            ulist = u_CONS
        else: #otros servicios
            ulist = u_OS
        
        for u in ulist:
            score = get_score(question, u, texts_data)
            ranking.append(score)
            
        if topic == "Consultoria":
            if np.max(ranking) >= 4:  #tunned parameter
                url_res = ulist[np.argmax(ranking)]            
                return url_res   
            else:
                return None
        elif np.max(ranking) > 0:
            url_res = ulist[np.argmax(ranking)]            
            return url_res
        else:
            return None           
        
    except Exception as e:
        print('Exception en suggest_url: {0}'.format(e))
        return None      

