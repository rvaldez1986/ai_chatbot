# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 08:21:31 2019

@author: sebastian.tamayo
"""

base_url= "http://192.168.1.15:8080/actuaria-business/api"

import requests
def consulta_ruc(ruc):
   headers  = {"Accept": "application/json", "authorization":"eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJhY3R1YXJpYS1idXNpbmVzcyIsIm5hbWUiOiJwb3J0YWwifQ.n8_EF7R7EKayhwU3Eu7IfTdyAgGdFgfuoCa871aSJ7AY8Xu4AHyInOSik8IOjQag_vULNwdtJOcAKxqWv3ZQLg"}
   URL= base_url+"/clientes/consulta-por-ruc/"+str(ruc)

   try:
        r = requests.get(url=URL,headers=headers)
        payload = r.json()
        answer = payload["respuesta"]["razonSocial"]
        codigo_cliente_ruc = payload["respuesta"]["codigoCliente"]
        return (answer,codigo_cliente_ruc)        

   except Exception:
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
    
#consulta_proc(55666)  
    

