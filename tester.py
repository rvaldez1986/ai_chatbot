# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 14:20:15 2019

@author: rober
"""

import os
os.chdir('C:\\Users\\rober\\desktop\\ai_chatbot')
    
from text_processer import proc_message
from textblob import TextBlob

#message = 'cuanto cuesta un estudio actuarial para una empresa pequena' 
#message = 'que mal servicio que dan' 
#message = 'cuanto cuesta un estudio de pasivo laboral'  
#message = 'cuanto cuesta un estudio de consultoria'
#message = 'cuanto cuesta un esudio del iess'
#message = 'hola'
#message = 'mi nombre es roberto valdez'
#message = 'No'
#message = 'mi correo es roberto.valdez.ponce@gmail.com'

#message = 'Hola, buenos dias, mi correo es roberto.valdez.ponce@gmail.com'

#message = 'es pesimo su servicio, mi correo es roberto.valdez.ponce@gmail.com'
message = 'roberto.valdez.ponce@gmail.com'

out_message = proc_message(message)
out_message


    
blob = TextBlob(message)
blob = blob.translate(to='en').lower()    


