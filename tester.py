# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 14:20:15 2019

@author: rober
"""

import os
os.chdir('C:\\Users\\rober\\desktop\\ai_chatbot')
    
from text_processer import proc_message
from collections import defaultdict
from textblob import TextBlob

users_dict = defaultdict(lambda: [0, None, None, None])


#message = 'cuanto cuesta un estudio actuarial para una empresa pequena' 
#message = 'que mal servicio que dan' 
#message = 'cuanto cuesta un estudio de pasivo laboral'  
#message = 'cuanto cuesta un estudio de consultoria'
#message = 'cuanto cuesta un esudio del iess'
message = 'hola'
#message = 'mi nombre es roberto valdez'
#message = 'No'
#message = 'mi correo es roberto.valdez.ponce@gmail.com'
#message = 'Hola, buenos dias, mi correo es roberto.valdez.ponce@gmail.com'
#message = 'es pesimo su servicio, mi correo es roberto.valdez.ponce@gmail.com'
#message = 'roberto.valdez.ponce@gmail.com'


recipient_id = 1

context = users_dict[recipient_id]
out_message, context = proc_message(message, context)
out_message
context

out_message, context = proc_message(message, context)
out_message


message = 'No'
   
blob = TextBlob(message)

if blob.detect_language() != 'en':

    blob = blob.translate(to='en').lower() 
    
    
#def set_greeting_text(self, text):
#        data = {"setting_type": "greeting", "greeting": {"text": text}}
#        fmt = self.graph_url + "me/thread_settings?access_token={token}"
#        return requests.post(fmt.format(token=self.access_token),
#                             headers={"Content-Type": "application/json"},
#                             data=json.dumps(data))

topics = ['jubilacion patronal', 'consultoria', 'recursos humanos', 'IESS']

rep = 'su tema {0} es el que tratamos'

print(rep.format(topics[0]))


