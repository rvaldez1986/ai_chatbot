# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 12:35:29 2019

@author: rober
"""

def dict_textos0():    
    textos = {}    
   
    #REPLYS
    repST  = ('¿Su consulta sobre {0} es realizada por una persona natural o jurídica (empresa)?')
    repQ   = ('Gracias por su retroalimentación. En ACTUARIA siempre nos esforzamos por dar el mejor servicio.  ¿Desea formalizar su queja?')    
    repHF  = ('Gracias por confiar en nosotros!')
    repJS  = ('Gracias por su interés, puede enviar su CV y una carta motivacional al siguiente correo: infouio@actuaria.com.ec')   
    repCN  = ('ACTUARIA cuenta con oficinas en Quito y Guayaquil. El teléfono en Quito es (02) 2-501-001 y el de Guayaquil es (04) 295-9204.'
              'La dirección de Quito es Orellana y 6 de Diciembre y en Guayaquil estamos ubicados en la Avenida Emilio Romero y Benjamín Carrión.'
              'En caso de requerir mayor información envíe un correo a: roberto.valdez@actuaria.com.ec o deje un mensaje en el siguiente link: https://www.actuaria.com.ec/contacto/')
    repGR  = ('Es un placer poder ayudarle. Por favor escriba el motivo de su consulta.')
    repCHAR = ('Para mayor información sobre charlas y capacitaciones, le invitamos a revisar el siguiente link: '
                'https://actuaria.com.ec/servicio/capacitaciones/ o para cualquier consulta por favor comuníquese al (02) 2-501-001 EXT-601 para ayudarle inmediatamente con toda la información necesaria.'
                'Para contactos por correo por favor escribir a charlas@actuaria.com.ec')
    repFAC = ('En caso de requerir asistencia para Facturación/Retención/Cobros por favor comuníquese al (02) 2-501-001 EXT-601 para ayudarle inmediatamente con toda la información necesaria.'
                'Para contactos por correo por favor escribir a facturacion@actuaria.com.ec')
    repNT  = ('Por favor especifique si su consulta es sobre un tema de ACTUARIA CONSULTORES o es sobre otro tema?')
    repCE  = ('En breves minutos, su requerimiento será enviado a un representante de ACTUARIA. Por favor espere en este chat para ser contestado. '
              'Si es un requerimiento urgente, por favor contactarse al (02) 2-501-001')  
    
    repU1T = ('Su consulta no es clara. Se refiere al tema {0}?') #revisar
    repU2T  = ('Su consulta trata principalmente sobre el tema: {0}, {1} o ninguno de los dos?') #revisar 
    repUNT  = ('Su consulta no es clara.\n'
               'Por favor intente reformular su consulta incluyendo el mayor número de detalles posible. '
               'Por ejemplo para el tema {0} puede incluir palabaras como {1}.') #revisar 
    
    
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
                       'trabaje con nosotros': 'hoja de vida, cv, currículum, etc.', 
                       'Facturacion/Retencion/Cobros': 'factura, retención, etc.'}   

    
    #FILL DICT  
    textos["ST"] = repST 
    textos["Queja"] = repQ 
    textos["Hi Five"] = repHF
    textos["trabaje con nosotros"] = repJS
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
    repST0   = ('ACTUARIA es una empresa especializada en la asesoría estratégica para personas jurídicas. \n \nSin embargo, para el tema: {0} hemos analizado '
                'su consulta y ponemos a su disposición el siguiente link: {1} en el cual podrá encontrar mayor información. '
                '\n \nPara simulaciones y cálculos por favor diríjase al siguiente link: https://actuaria.com.ec/simuladores/') #revisar
    repST1   = ('ACTUARIA es una empresa especializada en la asesoría estratégica para personas jurídicas. Sin embargo para el tema {0} si desea '
                'realizar simulaciones y cálculos por favor diríjase al siguiente link: https://actuaria.com.ec/simuladores/')    #revisar
    repST2   = ('Por favor ingrese el RUC de su empresa.')
    repST3   = ('Lo lamento, ¿su consulta sobre el tema {0} es para una persona natural o de una empresa?'
                '\n \nSi desea realizar otra consulta digite \'salir\' para volver al inicio.')    
    repST4   = ('No se pudo validar su respuesta. Muchas gracias por contactarnos.')
    repST5   = ('ACTUARIA es una empresa especializada en la asesoría estratégica para personas jurídicas. \n \nSin embargo, para el tema: {0} hemos analizado '
                'su consulta y ponemos a su disposición el siguiente link: {1} en el cual puede encontrar una posibe respuesta. '
                '\n \nPara simulaciones y cálculos por favor diríjase al siguiente link: https://actuaria.com.ec/simuladores/ \n \n'
                '¿Estaría interesado en recibir una asesoría especializada en temas del IESS por una hora con nuestros asesores para resolver sus inquietudes?') #revisar
    repQ0    = ('Por favor en un mismo mensaje detalle lo sucedido, seguido de su correo electrónico y número telefónico para contactarnos a la brevedad posible.')  
    repQ1    = ('Gracias por sus comentarios, los tendremos en cuenta para nuestro proceso de mejora continua.')  
    repQ2    = ('No fué posible validar su respuesta, ¿desea formalizar su queja? \n \nSi desea realizar otra consulta digite \'salir\' para volver al inicio.') 
    repNT0   = ('En breves minutos, su requerimiento será enviado a un representante de ACTUARIA. Por favor espere en este chat para ser contestado. Si es un requerimiento urgente, por favor contactarse al (02) 2-501-001') 
    repNT1  = ('\nEl cliente con id: {0} ha enviado al chatbot un mensaje que no pudo ser resuelto. El mensaje original fué: \n{1}')
    repNT2   = ('No fué posible validar su respuesta, el tema de su consulta es relativo a ACTUARIA CONSULTORES o a otro tema? \n \n'
                'Si desea realizar otra consulta digite \'salir\' para volver al inicio')#revisar
    repSalir = ('Por favor escriba el motivo de su nueva consulta.')
    
    #FILL DICT  
    textos["ST"] = [repST0, repST1, repST2, repST3 , repST4,repST5] 
    textos["Queja"] = [repQ0, repQ1, repQ2] 
    textos['NT'] = [repNT0, repNT1, repNT2]  
    textos['salir'] =  repSalir
    
    return textos

def dict_textos2():    
    textos = {}    
    
    #REPLYS
    repST0  = ('Gracias por ingresar su RUC. ¿Requiere el envío de una cotización?')
    repST1  = ('Gracias por ingresar su RUC. ¿Requiere información sobre un proceso que actualmente está realizando con ACTUARIA?')
    repST2  = ('Gracias por ingresar su RUC. ¿Requiere informacion sobre el tiempo de entrega de un estudio?')
    
    repST3  =  ('Gracias por ingresar su RUC. \n \nLo lamento, no se tiene una respuesta desarrollada su consulta. Este chat esta siendo enviado a un representante '
               'de ACTUARIA para el analisis necesario. Por favor espere en este chat para ser contestado. Si es un requerimiento urgente '
               'Por favor contactarse al (02) 2-501-001, para que su requerimiento sea atendido. \n \n Mientras tanto, en base al tema de su consulta '
               'se ha podido determinar que el siguiente link puede ser de su interés: {0}')#revisar
    
    repST4  =  ('Gracias por ingresar su RUC.\n \n Su requerimiento está siendo enviado a uno de nuestros asesores. '
               'Si es un requerimiento urgente por favor contactarse al (02) 2-501-001')#revisar
    
   
    repST5  = ('El RUC ingresado no es válido, ¿puede ingresarlo nuevamente? \n \nSi desea realizar otra consulta '
               'digite \'salir\' para volver al inicio.')
    repST6  = ('No se pudo validar su RUC. Muchas gracias por contactarnos.')
    repMSG  = ("\nEl chatbot recibio una queja formal de servicio con los siguientes datos y detalles:\n {0}" 
               " \n El mensaje original de queja fue:\n {1}"
               "\n Por Favor contactar de manera inmediata al cliente.\n") 
    repMSG1  = ('Muchas gracias por su tiempo. Hemos notificado al Departamento de satisfacción al cliente. Un asesor se comunicará con usted de forma inmediata.')   
    repSalir = ('Por favor escriba el motivo de su nueva consulta.')
    
    repMINTERNO = ('\nEl cliente con id: {0} ha enviado al chatbot un mensaje que no pudo ser resuelto. El mensaje original fué: \n{1}') 
    repPN0  = ('Perfecto, nos puede dejar un nombre y un correo para contactarnos y enviar la propuesta de asesoría?')
    repPN1  = ('Fue un placer ayudarle, esperamos que los enlaces hayan sido de su interés.')#revisar
    repPN2  = ('No fué posible validar su respuesta. ¿Estaría usted interesado en una asesoría sobre el tema IESS?')#revisar
    repPN3  = ('Muchas gracias por contactarnos.')
    
    #FILL DICT
    textos["ST"] = [repST0, repST1, repST2, repST3, repST4, repST5, repST6]     
    textos["MSG"] = [repMSG, repMSG1]  
    textos['salir'] =  repSalir
    textos['interno'] = repMINTERNO
    textos['PN'] = [repPN0, repPN1,repPN2, repPN3] 
    
    
    return textos

def dict_textos3():
    textos = {}    
    
    #REPLYS
    repST0  = ('Perfecto, nos puede dejar un nombre y un correo para contactarnos y enviar la propuesta de {0}?')
    repST1  = ('El tiempo de entrega de un estudio de {0} es de 8 días laborables contados a partir de la recepción de la información entregada por el cliente.') #revisar  
    repST2  = ('¿Requiere el envío de una cotización? \n \n'
               'Si desea realizar otra consulta digite \'salir\' para volver al inicio.')
    repST3  = ('¿Requiere información sobre un proceso que actualmente está realizando con ACTUARIA? \n \n'
               'Si desea realizar otra consulta digite \'salir\' para volver al inicio.')
    repKO  = ('{0} Por favor ingrese el número del proceso remitido por ACTUARIA. Si no cuenta con numero de proceso comuniquese al (02) 2-501-001 para ayudarle inmediatamente')
    repKO1  = ('No se ha podido encontrar el RUC en el sistema. Por favor contáctenos al (02) 2-501-001 para ayudarle inmediatamente.')#oportunidad de mejora
    repKO2  = ('En breves minutos, su requerimiento será enviado a un asesor de ACTUARIA para el análisis necesario. Por favor espere en este chat para ser contestado. Si es un requerimiento urgente '
               'por favor contactarse al (02) 2-501-001 para ayudarle inmediatamente.')
    repKO3  = ('\nEl cliente con id: {0} ha enviado al chatbot un mensaje que no pudo ser resuelto. El mensaje original fué: \n{1}')  
    repSalir = ('Por favor escriba el motivo de su nueva consulta.')

    
    #FILL DICT
    textos["ST"] = [repST0, repST1, repST2, repST3]      
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
    repKO1  = ('Su número de proceso no es correcto. Por favor comuniquese al (02) 2-501-001')    
    repKO2  = ('Número de proceso incorrecto, por favor ingrese nuevamente. \n \nSi desea realizar otra consulta digite \'salir\' para volver al inicio')
    repKO3  = ("\nEl chatbot recibió una consulta de un proceso datos y detalles:\n Proceso: {0}  Razón Social: {2}  Estado del Proceso: {3}  Código del Cliente: {4}" 
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
    
    repST2  = ('No se envió el correo')
    
    repMSG = ("\nSe envió al chatbot el requerimiento de una cotizacion con los siguientes datos: \n {0}")
    
    
    #FILL DICT
    textos["ST1"] = repST1
    textos["ST2"] = repST2
    textos["MSG"] = repMSG
    
    return textos
