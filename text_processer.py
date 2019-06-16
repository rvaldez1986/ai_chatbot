# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:29:38 2019

@author: rober
"""

from textblob import TextBlob
import numpy as np

def dict_reply():
    
    respuestas = {}
    
    #REPLY NEG POLARITY
    repNP = ('El objetivo de ACTUARIA es siempre mantener los estandares mas altos de satisfaccion del cliente. '
             'Este correo sera enviado directamente a nuestro departamento gerencial para realizar el analisis pertinente. '
             'Por favor ingrese su correo en este chat y nos contactaremos directamente con usted con el objetivo de '
             'solucionar cualquier inconveniente')    
    
    #REPLIES (TOPIC * NOUNS)
    
    rep0 = ('Para obtener mas informacion sobre jubilacion patronal por favor escribir un correo electronico '
            'a 123456@actuaria.com.ec o dejenos su correo en este chat y nos contactaremos '
            'inmediatamente con usted.')    
    
    rep1 = ('El precio de un estudio de jubilacion patronal se establece en terminos de el numero '
            'de trabajadores y la complejidad, para una cotizacion directa por favor escribir un correo electronico '
            'a 123456@actuaria.com.ec o dejenos su correo en este chat y nos contactaremos '
            'inmediatamente con usted.')
    
    rep2 = ('Para obtener mas informacion de el area de consultoria por favor escribir un correo electronico '
            'a 123456@actuaria.com.ec o dejenos su correo en este chat y nos contactaremos '
            'inmediatamente con usted.')    
    
    rep3 = ('El precio de un estudio de consultoria se establece en terminos de el tamaño de la empresa '
            'y la complejidad, para una cotizacion directa por favor escribir un correo electronico '
            'a 123456@actuaria.com.ec o dejenos su correo en este chat y nos contactaremos '
            'inmediatamente con usted.')
                   
    rep4 = ('Para obtener mas informacion sobre los estudios de compensaciones y/o recursos humanos '
            'por favor escribir un correo electronico a 123456@actuaria.com.ec o '
            'dejenos su correo en este chat y nos contactaremos inmediatamente con usted.')   
                   
    rep5 = ('El precio de un estudio de compensaciones y/o recursos humanos se establece en terminos de '
            'el tamaño de la empresa y la complejidad, para una cotizacion directa por favor escribir un '
            'correo electronico a 123456@actuaria.com.ec o dejenos su correo en este chat y nos contactaremos '
            'inmediatamente con usted.')    
                   
    rep6 = ('Para obtener informacion sobre temas relacionados al IESS por favor escribir un correo '
            'electronico a 123456@actuaria.com.ec o dejenos su correo en este chat y nos contactaremos '
            'inmediatamente con usted.')                
            
    rep7 = ('Para obtener informacion sobre posiciones vacantes y proximas entrevistas por favor enviar '
            'un correo a 123456@actuaria.com.ec o dejenos su correo en este chat y nos contactaremos '
            'inmediatamente con usted.')
                    
    #Mensaje no topic                    
    repNT = ('No se pudo validar su solicitud, por favor enviar un correo a 123456@actuaria.com.ec o '
             'dejenos su correo en este chat y nos contactaremos inmediatamente con usted.')
                    
    #Greeting message
    repgret = ('Hola, mi nombre es eC-BOT y soy un chatbot con inteligencia artificial elaborado por la '
             'division Actuaria-ai.')  
    
    lres = [rep0,rep1,rep2,rep3,rep4,rep5,rep6,rep6,rep7,rep7]    #for 6 and 7 not option for price            
    
    k = 0
    for i in range(5):
        for j in range(2):
            respuestas[(i,j)] = lres[k]
            k +=1
    
    respuestas['NP'] = repNP        
    respuestas['gret'] = repgret
    respuestas['NT'] = repNT
    
    return respuestas


def dict_topics():
    #Greeting?
    greeting_tokens = ["hello", "hi", "greetings", "good", "morning"]
    
    #Topic tokens
    tokens_estudio_jp = ['actuarial', 'employee', 'employer', 'company', 'retirement', 'labor', 'liabilities']
    tokens_consultoria = ['technical', 'note', 'insurance', 'prepaid', 'medicine', 'consulting', 'consult', 'consultancy',
                      'company', 'statistical', 'mathematical', 'math', 'analysis']
    tokens_rrhh = ['salary', 'level', 'compensation', 'wage', 'climate']
    tokens_iess = ['retirement', 'iess', 'disability', 'old', 'age', 'death', 'insurance']
    tokens_jobseeker = ['hiring', 'hire']
    
    #nouns
    price_nouns = ['price', 'cost']
    
    topics = {}
    topics['gt'] = greeting_tokens
    topics['jp'] = tokens_estudio_jp 
    topics['c'] = tokens_consultoria          
    topics['rrhh'] = tokens_rrhh
    topics['iess'] = tokens_iess
    topics['js'] = tokens_jobseeker
    topics['pn'] = price_nouns
    
    return topics


def proc_message(message): 
    
    #variables
    pol = 0
    gt = 0
    b = 0
    topic_l = np.array([0,0,0,0,0]) #0: jub-pat, 1: consultoria, 2: RRHH, 3: IESS, 4: JOB SEEKERS
    nouns = np.array([0]) #0: PRICE, MORE INFO
    ret_message = ''
    
    respuestas = dict_reply()
    topics = dict_topics()    
    
    try:    
            
        #translate and sentiment analysis    
        blob = TextBlob(message)
        blob = blob.translate(to='en').lower()    
        pol = blob.sentiment[0]
        
        #topic analysis    
        for w in blob.words:
            w1 = w.lemmatize() ; w2 = w
            if (w1 in topics['gt']) or (w2 in topics['gt']):
                gt += 1         
            if (w1 in topics['jp']) or (w2 in topics['jp']):
                topic_l[0] += 1
            if (w1 in topics['c']) or (w2 in topics['c']):
                topic_l[1] += 1
            if (w1 in topics['rrhh']) or (w2 in topics['rrhh']):   
                topic_l[2] += 1
            if (w1 in topics['iess']) or (w2 in topics['iess']):    
                topic_l[3] += 1
            if (w1 in topics['js']) or (w2 in topics['js']):   
                topic_l[4] += 1    
                
        #Noun analysis                
        blob_nouns = list()
        for word, tag in blob.tags:
            if tag == 'NN':
                blob_nouns.append(word.lemmatize())    
    
        for n in blob_nouns:
            if n in topics['pn']:
                nouns[0] += 1
            
        
        a  = np.argmax(topic_l)
        
        if nouns[0] > 0:
            b = 1
               
        
        if max(topic_l) > 0:
            r = respuestas[(a,b)]
        elif gt > 0:
            r = ''
        else:
            r = respuestas['NT']
        
        
        if pol < -0.05:
            ret_message = respuestas['NP']    
        else:
            if gt > 0:
                ret_message += respuestas['gret'] 
            
            ret_message += r
            
    except:
        
        ret_message =  respuestas['NT']   
    
    return ret_message