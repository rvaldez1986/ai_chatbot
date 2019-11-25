# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 12:14:34 2019

@author: rober
"""

import smtplib

fromaddr = "roberto.valdez@actuaria.com.ec"
toaddr = "roberto.valdez@actuaria.com.ec"
text = "Hello World"


server = smtplib.SMTP('smtp.gmail.com', 587)
#server.connect("smtp.gmail.com",465)
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromaddr, "XXX")
server.sendmail(fromaddr, toaddr, text)
server.quit()



import os

os.chdir('C:\\Users\\rober\\Desktop\\chatbot\\ai_chatbot')

from nlp_functions import send_email
import textos as txts

textos = txts.dict_textos4() 
        
message2 = ("\nSe envió al chatbot el requerimiento de una cotizacion con los siguientes datos: ").encode('utf-8')

toaddr = "roberto.valdez@actuaria.com.ec"
ret = send_email(message2, toaddr)










