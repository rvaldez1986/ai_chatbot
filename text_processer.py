# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:29:38 2019

@author: rober
"""

import random
from textblob import TextBlob


def proc_message(message):
    
    analysis = TextBlob(message)
    analysis = analysis.translate(to='en')
    pol = analysis.sentiment[0]
    
    
    if message == 'hola':
        sample_responses = ["hola soy un chatbot con ai"]
    elif pol > 0:
        #good message
        sample_responses = ["Que bueno que le guste nuestro servicio!", "Siempre para ayudar",
                                "Nuestro objetivo es siempre ser mejores!", "Gracias por ser nuestro cliente!"]
    elif pol < 0:
        #bad message
        sample_responses = ["Nuestro objetivo es la mjora continua, este mensaje sera tratado con prioridad alta \
                                por nuestro representante de atencion al cliente", "Gracias por contactarnos, disculpe el mal momento",
                                 "Vamos a intentar contactarnos con usted en la brevedad del caso"]
    else:
        sample_responses = ["Cuenteme en que le puedo ayudar", "En que podemos ayudarle hoy"]
    # return selected item to the user
    return random.choice(sample_responses)   





#analysis = TextBlob("que mal servicio que tienen, se demoran mucho en todo y no contestan el telefono")

#analysis = TextBlob("hola me llamo roberto")

#analysis = TextBlob("me pueden ayudar con un estudio de jubilacion patronal")


#analysis = TextBlob("muchas gracias por todo, actuaria es muy moderna")

#analysis = analysis.translate(to='en')

#print(analysis.sentiment[0])