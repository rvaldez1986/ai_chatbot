# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 12:35:29 2019

@author: rober
"""

def dict_textos0():    
    textos = {}    
   
    #REPLYS
    repST  = ('Su consulta sobre el tema {0} es para una persona natural o para una empresa?')
    repQ   = ('Gracias por su retroalimentacion. En ACTUARIA siempre nos esforzamos por dar el mejor servicio, sin embargo apreciamos mucho las oportunidades de mejora.  '
              'Desea formalizar su queja?')    
    repHF  = ('Gracias por confiar en nosotros!')
    repJS  = ('Gracias por su interes, puede enviar su cv y una carta motivacional al correo infouio@actuaria.com.ec')   
    repCN  = ('ACTUARIA tiene oficinas en Quito y Guayaquil. El telefono de Quito es (02) 2-501-001 y el telefono '
              'de Guayaquil es (04) 295-9204. La direccion de Quito es Orellana y 6 de Diciembre y en Guayaquil estamos ubicados en '
              'Emilio Romero y Benjamin Carrion.')
    repGR  = ('Hola!')
    repCHAR = ('Por favor comuniquese al (02) 2-501-001 EXT-601  para ayudarle inmediatamente con toda la información necesaria')
    repNT  = ('Hmm.. Este tema es relativo a ACTUARIA? O es de otro tema?')
    repCE  = ('Gracias por contactarnos, si desea deje su correo y/o numero de telefono y nos contactaremos con usted.')    
    
    #FILL DICT  
    textos["ST"] = repST 
    textos["Queja"] = repQ 
    textos["Hi Five"] = repHF
    textos["job seeker"] = repJS
    textos["Contacto"] = repCN
    textos["Greeting"] = repGR
    textos["Otros servicios (Charlas/Capacitaciones/Financiera)"] = repCHAR
    textos['NT'] = repNT
    textos['CE'] = repCE 
    
    return textos

def dict_textos1():   
    textos = {} 
    
    #REPLYS
    repST0   = ('Actuaria esta dirigida principalmente a servicio de empresas, sin embargo para el tema {0} esta a '
                'disposicion los siguientes links y blogs: {1} o si desea realizar simulaciones y calculos por favor '
                'dirijase a el siguiente link: https://actuaria.com.ec/simuladores/')
    repST1   = ('Actuaria esta dirigida principalmente a servicio de empresas, sin embargo para el tema {0} si desea '
                'realizar simulaciones y calculos por favor dirijase a el siguiente link: https://actuaria.com.ec/simuladores/')    
    repST2   = ('Por favor puede ingresar el RUC de su empresa?')
    repST3   = ('No entendi. Su consulta sobre el tema {0} es para una persona natural o de una empresa?')    
    repQ0    = ('Por favor en un mismo mensaje detalle lo sucedido, seguido de su correo electronico y número telefónico para contactarnos a la brevedad posible.')  
    repQ1    = ('Gracias por sus comentarios, lo tendremos en cuenta para nuestro proceso de mejora continua.')  
    repQ2    = ('No entendi su respuesta, desea formalizar su queja?')  
    repNT0   = ('No entendi su inquietud, Podria por favor reformular su pregunta expresando con mas detalle sus necesidades') 
    repNT1   = ('No entendi su respuesta, el tema es relativo a ACTUARIA o a otro tema?')
    
    #FILL DICT  
    textos["ST"] = [repST0, repST1, repST2, repST3] 
    textos["Queja"] = [repQ0, repQ1, repQ2] 
    textos['NT'] = [repNT0, repNT1]    
    
    return textos

def dict_textos2():    
    textos = {}    
    
    #REPLYS
    repST0  = ('Requiere el envio de una cotizacion?')
    repST1  = ('Requiere informacion sobre un proceso que actualmente esta realizando con ACTUARIA?')
    repST2  = ('Lo lamento, no entendi su requerimiento. Pero sigo aprendiendo. Por favor podria explicarme a mayor detalle su requerimiento?'
               'Caso contrario si se comunica con nosotros al (02) 2-501-001 con mucho gusto le ayudaremos.')
    repST3  = ('El RUC ingresado no es valido, puede ingresar nuevamente el RUC de su empresa?')
    repMSG  = ("\nEl chatbot recibio una queja formal de servicio con los siguientes datos y detalles:\n {0}" 
               " \n El mensaje original de queja fue:\n {1}"
               "\n Por Favor contactar de manera inmediata al cliente.\n") 
    repMSG1  = ('Muchas gracias por su tiempo. Hemos notificado al departamento de satisfaccion al cliente. '
              'Un asesor se comunicará con usted en breve.')    
    repMSG2  = ('Oppps, no pudimos enviar el correo a nuestro departamento de satisfaccion al cliente, sin embargo fueron notificados y pronto se contactaran con usted.')
    
    #FILL DICT
    textos["ST"] = [repST0, repST1, repST2, repST3]     
    textos["MSG"] = [repMSG, repMSG1, repMSG2]  
    
    
    return textos

def dict_textos3():
    textos = {}    
    
    #REPLYS
    repST0  = ('Perfecto, nos puede dejar un nombre y un correo para contactarnos y enviar la propuesta de {0}?')
    repST1  = ('No entendi su respuesta, requiere envio de una cotizacion?')
    repST2  = ('No entendi su respuesta, requiere informacion sobre un proceso que actualmente esta realizando con ACTUARIA?')
    repKO  = ('Hola {0} ¿Por favor puede ingresar el numero del proceso enviado al correo de la persona encargada en su empresa?')
    repKO1  = ('Oppps, no puedo encontrar su RUC en el sistema. Por favor contactenos al (02) 2-501-001 para ayudarle inmediatamente')
    repKO2  = ('Lo lamento, no puedo entender su requerimiento pero sigo aprendiendo. Por favor contactarse al (02) 2-501-001 para ayudarle inmediatamente')    
    
    #FILL DICT
    textos["ST"] = [repST0, repST1, repST2]      
    textos["KO"] = [repKO, repKO1, repKO2]  
    
    return textos


def dict_textos4():
    textos = {}    
    
    #REPLYS
    repMSG = ("\nSe envió al chatbot el requerimiento de una cotizacion con los siguientes datos: \n {0}")
    repMSG1  = ('Muchas gracias, se ha enviado un correo a nuestro departamento de comercial con sus datos y '
              'nos contactaremos con usted en la brevedad posible')    
    repMSG2  = ('Oppps, no pudimos enviar el correo a nuestro departamento comercial, sin embargo fueron notificados y pronto se contactaran con usted.')    
    
    
    repKO  = ('Estimado {0} Su proceso se encuentra {1}, el encargado de su estudio es {2}, Los datos de contacto son email: {3}. Telefono (02)-2501001 extension {4}.'
              '  Ademas hemos notificado al encargado de su cuenta a que se comunique con usted a la brevedad posible')
    repKO1  = ('Su numero de proceso no es correcto. Por favor comuniquese al (02) 2-501-001')    
    repKO2  = ('Numero de Proceso incorrecto, por favor ingrese nuevamente su proceso:')
    repKO3  = ("\nEl chatbot recibio una consulta de un proceso datos y detalles:\n Proceso: {0}  Razon Social: {2}  Estado del Proceso: {3}  Codigo del Cliente: {4}" 
               " \n El mensaje original de consulta fue:\n {1}"
               "\n Por Favor contactar de manera inmediata al cliente.\n") 
    repKO4  = ('Ademas hemos notificado al encargado de su cuenta a que se comunique con usted a la brevedad posible')    
    repKO5  = ('Oppps, no pudimos enviar el correo al encargado de su cuenta, sin embargo fueron notificados y pronto se contactaran con usted.')
    
    #FILL DICT
    textos["MSG"] = [repMSG, repMSG1, repMSG2]
    textos["KO"] = [repKO, repKO1, repKO2,repKO3,repKO4,repKO5] 
    
    return textos


def dict_textos5():
    textos = {}    
    
    #REPLYS
    repST1  = ('Muchas gracias, se ha enviado un correo a nuestro departamento de pricing con sus datos y '
              'nos contactaremos con usted en la brevedad posible')
    
    repST2  = ('No se envio el correo')
    
    repMSG = ("\nSe envió al chatbot el requerimiento de una cotizacion con los siguientes datos: \n {0}")
    
    
    #FILL DICT
    textos["ST1"] = repST1
    textos["ST2"] = repST2
    textos["MSG"] = repMSG
    
    return textos
