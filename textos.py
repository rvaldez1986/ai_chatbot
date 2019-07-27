# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 12:35:29 2019

@author: rober
"""

def dict_textos0():    
    textos = {}    
   
    #REPLYS
    repST  = ('Su consulta sobre el tema {0} es para una persona natural o para una empresa?')
    repQ   = ('Gracias por su retroalimentacion. En ACTUARIA queremos siempre dar el mejor servicio. '
              'Desea formalizar su queja?')    
    repHF  = ('Gracias por confiar en nosotros!')
    repJS  = ('Gracias por su interes, puede enviar su cv y una carta motivacional al correo 123@actuaria.com.ec')   
    repCN  = ('ACTUARIA tiene oficinas en quito y guayaquil. El telefono de quito es 2-501-001 y el telefono '
              'de Guayaquil es 2-501-001. La direccion de Quito es Orellana y 6 de Diciembre y en Guayaquil es '
              'Emilio Romero y Benjamin Carrion.')
    repGR  = ('Hola!')
    repCHAR = ('Para charlas hay que desarrollar la info de horarios, hasta aca nomas esta hecho')
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
                'disposicion los siguientes links y blogs: www.actuaria.com.ec\link1')
    repST1   = ('Por favor puede ingresar el RUC de su empresa?')
    repST2   = ('No entendi. Su consulta sobre el tema {0} es para una persona natural o de una empresa?')    
    repQ0    = ('Si quere anadir algo a su queja, esto sera analizado directamente por el departamento de satisfaccion '
                'del cliente. De manera adicional nos puede incluir un correo electronico para contactarnos con usted.')  
    repQ1    = ('Gracias por sus comentarios, lo tendremos en cuenta para nuestro proceso de mejora continua.')  
    repQ2    = ('No entendi su respuesta, desea formalizar su queja?')  
    repNT0   = ('Gracias por contactarnos, si desea deje su correo y/o numero de telefono y nos contactaremos con usted.') 
    repNT1   = ('No entendi su respuesta, el tema es relativo a ACTUARIA o a otro tema?')
    
    #FILL DICT  
    textos["ST"] = [repST0, repST1, repST2] 
    textos["Queja"] = [repQ0, repQ1, repQ2] 
    textos['NT'] = [repNT0, repNT1]    
    
    return textos

def dict_textos2():    
    textos = {}    
    
    #REPLYS
    repST0  = ('Requiere el envio de una cotizacion?')
    repST1  = ('Requiere informacion sobre un proceso que actualmente esta realizando con ACTUARIA?')
    repST2  = ('No se encontro intent, Hasta aca nomas esta hecho')
    repST3  = ('El RUC ingresado no es valido, puede ingresar el RUC de su empresa?')
    repQ    = ('Muchas gracias por su tiempo. Vamos a analizar el contenido de sus comentarios y nos ponemos en '
              'contacto con usted')    
    
    #FILL DICT
    textos["ST"] = [repST0, repST1, repST2, repST3]     
    textos["Queja"] = repQ 
    
    
    return textos

def dict_textos3():
    textos = {}    
    
    #REPLYS
    repST0  = ('Perfecto, nos puede dejar un nombre y un correo para contactarnos y enviar la propuesta de {0}?')
    repST1  = ('Aqui se debe hacer una consulta al API de KOHINOR')
    repST2  = ('No se encontro intent, Hasta aca nomas esta hecho (se puede unir con estado anterior)')
    repST3  = ('No entendi su respuesta, requiere envio de una cotizacion?')
    repST4  = ('No entendi su respuesta, requiere informacion sobre un proceso que actualmente esta realizando con ACTUARIA?')
    
    #FILL DICT
    textos["ST"] = [repST0, repST1, repST2, repST3, repST4]      
    
    return textos





def dict_textos4():
    textos = {}    
    
    #REPLYS
    repST  = ('Muchas gracias, nos contactaremos con usted en la brevedad posible')
    
    
    #FILL DICT
    textos["ST"] = repST
    
    return textos
