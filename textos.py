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
              'Emilio Romero y Benjamin Carrion.\n Para contactos por correo por favor escribir a roberto.valdez@actuaria.com.ec. '
              'Por último puede dejarnos un mensaje por el siguiente link: https://www.actuaria.com.ec/contacto/')
    repGR  = ('Es un placer poder ayudarle. Por favor escriba el motivo de su consulta.')
    repCHAR = ('Para el tema de charlas y capacitaciones puede reviar la información en el siguiente link: '
               'https://actuaria.com.ec/servicio/capacitaciones/ o para cualquier consulta por favor '
               'comuniquese al (02) 2-501-001 EXT-601 para ayudarle inmediatamente con toda la información necesaria \n '
               'Para contactos por correo por favor escribir a charlas@actuaria.com.ec')
    repFAC = ('Para el tema de Facturacion/Retencion/Cobros por favor comuniquese al (02) 2-501-001 EXT-601 para ayudarle inmediatamente con toda la información necesaria \n '
               'Para contactos por correo por favor escribir a facturacion@actuaria.com.ec')
    repNT  = ('Por favor especifique si su consulta es sobre un tema de ACTUARIA CONSULTORES o es sobre otro tema?')
    repCE  = ('En breves minutos, su requerimiento será enviado a un representante de ACTUARIA. Por favor espere en este chat para ser contestado. '
              'Si es un requerimiento urgente, por favor contactarse al (02) 2-501-001')  
    
    repU1T = ('No estoy muy claro con su consulta. Se refiere al tema {0}?')
    repU2T  = ('Su consulta trata sobre el tema: {0}, {1} o ninguno de los dos?')  
    repUNT  = ('No me queda muy claro el tema de su mensaje. Por favor intente reformular su consulta incluyendo el mayor número de detalles posible. '
               'Por ejemplo para el tema {0} puede incluir palabaras como {1}.')  
    
    
    palabras_topic = {'Jubilacion Patronal': 'jubilación, patronal, estudio actuarial, etc.', 
                      'Consultoria': 'nota técnica, reserva ibnr, recursos humanos, etc.', 
                       'Renuncia/Despido/Desahucio': 'renuncia, despido, desahucio, desvinculación, etc.', 
                       'IESS': 'IESS, jubilación por vejez, invalidez o muerte, etc.', 
                       'Greeting': 'hola, buenos días, etc.', 
                       'Contacto': 'dirección, teléfono, correo, etc.', 
                       'Queja': 'queja, reclamo, etc.', 
                       'Otros servicios': 'consultoría financiera, precios de transferencia, avaluos, etc.', 
                       'Charlas/Capacitaciones': 'charla, capacitación, etc.', 
                       'Hi Five': 'buen servicio, muchas gracias, etc.', 
                       'job seeker': 'hoja de vida, cv, currículum, etc.', 
                       'Facturacion/Retencion/Cobros': 'factura, retención, etc.'}   

    
    #FILL DICT  
    textos["ST"] = repST 
    textos["Queja"] = repQ 
    textos["Hi Five"] = repHF
    textos["job seeker"] = repJS
    textos["Contacto"] = repCN
    textos["Greeting"] = repGR
    textos['Charlas/Capacitaciones'] = repCHAR
    textos['Facturacion/Retencion/Cobros'] = repFAC
    textos['NT'] = repNT
    textos['CE'] = repCE 
    textos["U1T"] = repU1T
    textos["U2T"] = repU2T
    textos["UNT"] = repUNT
    textos["palabras"] = palabras_topic
    
    return textos

def dict_textos1():   
    textos = {} 
    
    #REPLYS
    repST0   = ('Actuaria esta dirigida principalmente a servicio de empresas, sin embargo para el tema {0} hemos analizado '
                'su consulta y ponemos a su disposicion el siguiente link: {1} en el cual puede encontrar una posibe respuesta. '
                'Para simulaciones y calculos por favor dirijase al siguiente link: https://actuaria.com.ec/simuladores/')
    repST1   = ('Actuaria esta dirigida principalmente a servicio de empresas, sin embargo para el tema {0} si desea '
                'realizar simulaciones y calculos por favor dirijase a el siguiente link: https://actuaria.com.ec/simuladores/')    
    repST2   = ('Por favor puede ingresar el RUC de su empresa?')
    repST3   = ('No se pudo validar su respuesta. Su consulta sobre el tema {0} es para una persona natural o de una empresa? '
                '\n \nSi desea realizar otra consulta digite \'salir\' para volver al inicio.')    
    repST4   = ('No se pudo validar su respuesta. Muchas gracias por contactarnos.')
    repQ0    = ('Por favor en un mismo mensaje detalle lo sucedido, seguido de su correo electronico y número telefónico para contactarnos a la brevedad posible.')  
    repQ1    = ('Gracias por sus comentarios, lo tendremos en cuenta para nuestro proceso de mejora continua.')  
    repQ2    = ('No se pudo validar su respuesta, desea formalizar su queja? \n \nSi desea realizar otra consulta digite \'salir\' para volver al inicio.') 
    repNT0   = ('En breves minutos, su requerimiento será enviado a un representante de ACTUARIA. Por favor espere en este chat para ser contestado. Si es un requerimiento urgente, por favor contactarse al (02) 2-501-001') 
    repNT1  = ('\nEl cliente con id: {0} ha enviado al chatbot un mensaje que no pudo ser resuelto. El mensaje original fué: \n{1}')
    repNT2   = ('No se pudo validar su respuesta, el tema de su consulta es relativo a ACTUARIA CONSULTORES o a otro tema? \n \n'
                'Si desea realizar otra consulta digite \'salir\' para volver al inicio')
    repSalir = ('Por favor escriba el motivo de su nueva consulta.')
    
    #FILL DICT  
    textos["ST"] = [repST0, repST1, repST2, repST3 , repST4] 
    textos["Queja"] = [repQ0, repQ1, repQ2] 
    textos['NT'] = [repNT0, repNT1, repNT2]  
    textos['salir'] =  repSalir
    
    return textos

def dict_textos2():    
    textos = {}    
    
    #REPLYS
    repST0  = ('Requiere el envio de una cotizacion?')
    repST1  = ('Requiere informacion sobre un proceso que actualmente esta realizando con ACTUARIA?')
    repST2  = ('Lo lamento, no entendi su requerimiento. Pero sigo aprendiendo. Por favor podria explicarme a mayor detalle su requerimiento?'
               'Caso contrario si se comunica con nosotros al (02) 2-501-001 con mucho gusto le ayudaremos.')
    repST3  = ('El RUC ingresado no es valido, puede ingresar nuevamente el RUC de su empresa? \n \nSi desea realizar otra consulta '
               'digite \'salir\' para volver al inicio.')
    repST4  = ('No se pudo validar su RUC. Muchas gracias por contactarnos.')
    repMSG  = ("\nEl chatbot recibio una queja formal de servicio con los siguientes datos y detalles:\n {0}" 
               " \n El mensaje original de queja fue:\n {1}"
               "\n Por Favor contactar de manera inmediata al cliente.\n") 
    repMSG1  = ('Muchas gracias por su tiempo. Hemos notificado al departamento de satisfaccion al cliente. '
              'Un asesor se comunicará con usted en breve.')   
    repSalir = ('Por favor escriba el motivo de su nueva consulta.')
    
    
    #FILL DICT
    textos["ST"] = [repST0, repST1, repST2, repST3, repST4]     
    textos["MSG"] = [repMSG, repMSG1]  
    textos['salir'] =  repSalir
    
    
    return textos

def dict_textos3():
    textos = {}    
    
    #REPLYS
    repST0  = ('Perfecto, nos puede dejar un nombre y un correo para contactarnos y enviar la propuesta de {0}?')
    repST1  = ('No se pudo validar su respuesta. ¿Requiere el envío de una cotización? \n \n'
               'Si desea realizar otra consulta digite \'salir\' para volver al inicio.')
    repST2  = ('No se pudo validar su respuesta. ¿Requiere información sobre un proceso que actualmente está realizando con ACTUARIA? \n \n'
               'Si desea realizar otra consulta digite \'salir\' para volver al inicio.')
    repKO  = ('{0} Por favor ingrese el número del proceso remitido por ACTUARIA. Si no cuenta con numero de proceso comuniquese al (02) 2-501-001 para ayudarle inmediatamente')
    repKO1  = ('No se ha podido encontrar el RUC en el sistema. Por favor contáctenos al (02) 2-501-001 para ayudarle inmediatamente.')
    repKO2  = ('Lo lamento, no puedo entender su requerimiento pero sigo aprendiendo. Este chat esta siendo enviado a un representante '
               'de ACTUARIA para el analisis necesario. Por favor espere en este chat para ser contestado. Si es un requerimiento urgente '
               'Por favor contactarse al (02) 2-501-001 para ayudarle inmediatamente.')
    repKO3  = ('\nEl cliente con id: {0} ha enviado al chatbot un mensaje que no pudo ser resuelto. El mensaje original fué: \n{1}')  
    repSalir = ('Por favor escriba el motivo de su nueva consulta.')
    
    #FILL DICT
    textos["ST"] = [repST0, repST1, repST2]      
    textos["KO"] = [repKO, repKO1, repKO2, repKO3]  
    textos['salir'] =  repSalir
    
    return textos


def dict_textos4():
    textos = {}    
    
    #REPLYS
    repMSG = ("\nSe envió al chatbot el requerimiento de una cotizacion con los siguientes datos: \n {0}")
    repMSG1  = ('Muchas gracias, se ha enviado un correo a nuestro departamento de comercial con sus datos y '
              'nos contactaremos con usted en la brevedad posible.')    
    repMSG2  = ('Su requerimiento ha sido enviado al Departamento Comercial y muy pronto un ejecutivo se contactará con usted.')    
    repKO  = ('{0} Su proceso se encuentra ( {1} ), el encargado de su estudio es {2}, Los datos de contacto son email: {3}. Telefono (02)-2501001 extension {4}.'
              '  Ademas hemos notificado al encargado de su cuenta a que se comunique con usted a la brevedad posible.')
    repKO1  = ('Su numero de proceso no es correcto. Por favor comuniquese al (02) 2-501-001')    
    repKO2  = ('Numero de Proceso incorrecto, por favor ingrese nuevamente su proceso. \n \nSi desea realizar otra consulta digite \'salir\' para volver al inicio')
    repKO3  = ("\nEl chatbot recibio una consulta de un proceso datos y detalles:\n Proceso: {0}  Razon Social: {2}  Estado del Proceso: {3}  Codigo del Cliente: {4}" 
               " \n El mensaje original de consulta fue:\n {1}"
               "\n Por Favor contactar de manera inmediata al cliente.\n") 
    repKO4  = ('Hemos notificado al encargado de su cuenta a que se comunique con usted a la brevedad posible')    
    repKO5  = ('El encargado de su proceso tomará contacto con usted a la brevedad posible.')
    repKO6  = ('{0} Su proceso fue ( {1} ), el encargado de su estudio fue {2}, Los datos de contacto son email: {3}. Telefono (02)-2501001 extension {4}.'
              '  Ademas hemos notificado al encargado actual su cuenta a que se comunique con usted a la brevedad posible.')
    
    #FILL DICT
    textos["MSG"] = [repMSG, repMSG1, repMSG2]
    textos["KO"] = [repKO, repKO1, repKO2,repKO3,repKO4,repKO5,repKO6]
    
    return textos


def dict_textos5():
    textos = {}    
    
    #REPLYS
    repST1  = ('Muchas gracias. Se ha enviado su correo a nuestro Departamento Comercial. Nos contactaremos con usted a la brevedad posible.')
    
    repST2  = ('No se envio el correo')
    
    repMSG = ("\nSe envió al chatbot el requerimiento de una cotizacion con los siguientes datos: \n {0}")
    
    
    #FILL DICT
    textos["ST1"] = repST1
    textos["ST2"] = repST2
    textos["MSG"] = repMSG
    
    return textos
