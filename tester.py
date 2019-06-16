# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 14:20:15 2019

@author: rober
"""

import os
os.chdir('C:\\Users\\rober\\desktop\\ai_chatbot')
    
import numpy as np    
from text_processer import proc_message
from textblob import TextBlob

message = 'cuanto cuesta un estudio actuarial para una empresa pequena' 
#message = 'que mal servicio que dan' 
#message = 'cuanto cuesta un estudio de pasivo laboral'  
#message = 'cuanto cuesta un estudio de consultoria'
#message = 'cuanto cuesta un esudio del iess'
#message = 'hola'
#message = 'mi nombre es roberto valdez'
#message = 'No'


out_message = proc_message(message)
out_message


   
#message = 'cuanto cuesta un estudio actuarial para una empresa pequena' 
#message = 'que mal servicio que dan' 
#message = 'cuanto cuesta un esudio del iess'
message = 'mi correo es roberto.valdez@gmail.com'
#message = 'No'
    
blob = TextBlob(message)
blob = blob.translate(to='en').lower()    

for s in str(blob):
    if s == '@':
        print(s)
