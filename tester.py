# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 14:20:15 2019

@author: rober
"""
#context = [Estado: 0, Topic: NA, Polarity: NA, OM: NA, Intent: NA, Counter: 0, RUC:NA, Numproc:NA]  
import os
os.chdir('C:/Users/sebastian.tamayo/Desktop/chatbot_server')
    
from text_processer import proc_message
from collections import defaultdict
from textblob import TextBlob


users_dict = defaultdict(lambda: [0, None, None, None, None, 0,None,None])


import nlp_functions as nlp


#nlp.azure_q1('salir')
#nlp.proc_message1ST('estoy escribiendo a nombre de la empresa ..')


#nlp.pred_prob('quien es lionel messi?')

#nlp.proc_wiki('quien es lionel messi?')

#message = 'cuanto cuesta un estudio actuarial para una empresa pequena' 
#message = "quisiera informacion de mi proceso de jubilacion patronal"
#message = 'cuanto cuesta un estudio de pasivo laboral'  
#message = 'cuanto cuesta un estudio de consultoria'
#message = 'cuanto cuesta un esudio del iess'
#message = 'hola'
#message = 'mi nombre es roberto valdez'
#message = 'No'
#message = 'mi correo es roberto.valdez.ponce@gmail.com'
#message = 'Hola, buenos dias, mi correo es roberto.valdez.ponce@gmail.com'
#message = 'es pesimo su servicio, mi correo es roberto.valdez.ponce@gmail.com'
#message = 'roberto.valdez.ponce@gmail.com'

#message = 'Persona Natural'

#flujo de conversacion prueba

#message = "quisiera informacion de mi proceso de jubilacion patronal"
#context = [0,None,None,None,None,0,None,None]

#context = [1,'Jubilacion Patronal',0.0,'quisiera informacion de mi proceso de jubilacion patronal',None,1,None,None]
#message = "empresa"

message= "sebastiantamayo3@gmial.cpom"
context = [4,"IESS",-0.024999999999999994, 'necesito calcular mi pension del iess tenog 30 aportaciones',"reqCotizacion",0,None,None,"persona"]
client_id="123"
#context = [1,"Jubilacion Patronal",0.0, 'quisiera informacion del calculo de jubilacion patronal',None,None,None,None]

#message= "123456789123"
#context = [,"Jubilacion Patronal",-0.024999999999999994, 'quisiera informacion de mi proceso',"reqCurrProcInfo",0,"0190333515001",None]

#context = [4,"Jubilacion Patronal",-0.024999999999999994, 'quisiera informacion de mi proceso',"reqCurrProcInfo",0,"0190333515001",None]



out_message, context = proc_message(message, context,client_id)
out_message
context

out_message, context = proc_message(message, context,client_id)
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


