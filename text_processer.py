# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:29:38 2019

@author: rober
"""

from textblob import TextBlob
import numpy as np


def proc_message(message):
    
    #Greeting?
    greeting_tokens = ["hello", "hi", "greetings", "good", "morning"]
    
    #Topic tokens
    tokens_estudio_jp = ['actuarial', 'employee', 'employer', 'company', 'retirement']
    tokens_consultoria = ['technical', 'note', 'insurance', 'prepaid', 'medicine', 'consulting', 'consult',
                          'company', 'statistical', 'mathematical', 'math', 'analysis']
    tokens_rrhh = ['salary', 'level', 'compensation', 'wage', 'climate']
    tokens_iess = ['retirement', 'iess', 'disability', 'old', 'age', 'death', 'insurance']
    tokens_jobseeker = ['hiring', 'hire']
    
    #nouns
    price_nouns = ['price', 'cost']
    
    
    #variables
    pol = 0
    gt = 0
    topics = np.array([0,0,0,0,0]) #0: jub-pat, 1: consultoria, 2: RRHH, 3: IESS, 4: JOB SEEKERS
    nouns = np.array([0]) #0: PRICE, MORE INFO
    ret_message = ''
    
    #REPLY BAD POLARITY
    rep = 'El objetivo de ACTUARIA es siempre mantener los estandares mas altos de satisfaccion del cliente. \
    Este correo sera enviado directamente a nuestro departamento gerencial para realizar el analisis pertinente. \
    Por favor ingrese su correo en este chat y nos contactaremos directamente con usted con el objetivo de \
    solucionar cualquier inconveniente'    
    
    
    #REPLIES (TOPIC * NOUNS)
    
    rep0 = 'Para obtener mas informacion sobre jubilacion patronal por favor escribir un correo electronico \
    a 123456@actuaria.com.ec o dejenos su correo en este chat y nos contactaremos \
    inmediatamente con usted.'    
    
    rep1 = 'El precio de un estudio de jubilacion patronal se establece en terminos de el numero \
    de trabajadores y la complejidad, para una cotizacion directa por favor escribir un correo electronico \
    a 123456@actuaria.com.ec o dejenos su correo en este chat y nos contactaremos \
    inmediatamente con usted.'
    
    rep2 = 'Para obtener mas informacion de el area de consultoria por favor escribir un correo electronico \
    a 123456@actuaria.com.ec o dejenos su correo en este chat y nos contactaremos \
    inmediatamente con usted.'    
    
    rep3 = 'El precio de un estudio de consultoria se establece en terminos de el tamaño de la empresa\
    y la complejidad, para una cotizacion directa por favor escribir un correo electronico\
    a 123456@actuaria.com.ec o dejenos su correo en este chat y nos contactaremos\
    inmediatamente con usted.'
                   
    rep4 = 'Para obtener mas informacion sobre los estudios de compensaciones y/o recursos humanos \
    por favor escribir un correo electronico a 123456@actuaria.com.ec o \
    dejenos su correo en este chat y nos contactaremos inmediatamente con usted.'   
                   
    rep5 = 'El precio de un estudio de compensaciones y/o recursos humanos se establece en terminos de el tamaño de la empresa \
                   y la complejidad, para una cotizacion directa por favor escribir un correo electronico\
                   a 123456@actuaria.com.ec o dejenos su correo en este chat y nos contactaremos \
                   inmediatamente con usted.'    
                   
    rep6 = 'Para obtener informacion sobre temas relacionados al IESS por favor escribir un correo\
                electronico a 123456@actuaria.com.ec o\
                    dejenos su correo en este chat y nos contactaremos inmediatamente con usted.'                
            
    rep7 = 'Para obtener informacion sobre posiciones vacantes y proximas entrevistas por favor enviar \
                un correo a 123456@actuaria.com.ec o\
                    dejenos su correo en este chat y nos contactaremos inmediatamente con usted.'
                    
    #Mensaje no topic                    
    repm1 = 'No se pudo validar su solicitud, por favor enviar \
                un correo a 123456@actuaria.com.ec o\
                    dejenos su correo en este chat y nos contactaremos inmediatamente con usted.'
                    
    #Greeting message
    repgt = 'Hola, mi nombre es eC-BOT y soy un chatbot con \
                                inteligencia artificial elaborado por la division Actuaria-ai. '
                   
    
    
    lres = [rep0,rep1,rep2,rep3,rep4,rep5,rep6,rep6,rep7,rep7]    #for 6 and 7 not option for price            
    respuestas = {}
    k = 0
    for i in range(5):
        for j in range(2):
            respuestas[(i,j)] = lres[k]
            k +=1
    
    #process    
    blob = TextBlob(message)
    blob = blob.translate(to='en').lower()    
    pol = blob.sentiment[0]

    for w in blob.words:
        w = w.lemmatize()
        if w in greeting_tokens:
            gt += 1

    for w in blob.words:
        w = w.lemmatize()
        if w in tokens_estudio_jp:
            topics[0] += 1
        if w in tokens_consultoria:
            topics[1] += 1
        if w in tokens_rrhh:
            topics[2] += 1
        if w in tokens_iess:
            topics[3] += 1
        if w in tokens_jobseeker:
            topics[4] += 1


    blob_nouns = list()
    for word, tag in blob.tags:
        if tag == 'NN':
            blob_nouns.append(word.lemmatize())


    for n in blob_nouns:
        if n in price_nouns:
            nouns[0] += 1
        
    
    a  = np.argmax(topics)
    
    if nouns[0] > 0:
        b = 1
    else:
        b = 0
    
    if max(topics) > 0:
        r = respuestas[(a,b)]
    elif gt > 0:
        r = ''
    else:
        r = repm1
    
    
    if pol < 0:
        ret_message = rep        
    else:
        if gt > 0:
            ret_message += repgt
        
        ret_message += r
        
    
    return ret_message