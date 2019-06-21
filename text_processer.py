# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:29:38 2019

@author: rober
"""

from textblob import TextBlob
import numpy as np

def dict_textos0():    
    textos = {}    
    #Topics
    topics = ['jubilacion patronal', 'consultoria', 'recursos humanos', 'IESS']
    
    #REPLYS
    repNP = ('Desea presentar una queja formal? (SI/NO)') 
    repTop = ('Su consulta sobre el tema {0} es para una persona natural o de una empresa? (Persona Natural\Empresa)')
    repJS = ('Gracias por su interes, puede enviar su cv y una carta motivacional al correo 123@actuaria.com.ec')
    repGT = ('Hola!')
    repNT = ('No entendi. Puede repetir?')
    
    #FILL DICT
    textos['top'] = topics
    textos['NP'] = repNP    
    textos['RT'] = repTop
    textos['JS'] = repJS
    textos['GT'] = repGT
    textos['NT'] = repNT
    
    return textos

def dict_textos1():    
    textos = {}    
    #Topics
    topics = ['jubilacion patronal', 'consultoria', 'recursos humanos', 'IESS']
    
    #REPLYS
    repNP1   = ('Por favor ingrese sus datos y si quere anadir algo a su queja, esto sera analizado '
               'directamente por el departamento de satisfaccion del cliente.') 
    repNP2   = ('Gracias por sus comentarios, lo tendremos en cuenta para nuestro proceso de mejora continua.') 
    repNT1   = ('No entendi. Desea presentar una queja formal? (SI/NO)')
    
    repPERS  = ('Actuaria esta dirigida principalmente a servicio de empresas, sin embargo para el tema {0} esta a '
               'disposicion los siguientes links y blogs: www.actuaria.com.ec\link1')
    repEMP   = ('Por favor puede ingresar: (ruc, telefono, …) de su empresa?')
    repNT2   = ('No entendi. Su consulta sobre el tema {0} es para una persona natural o de una '
                'empresa? (Persona Natural\Empresa)')
    
    #FILL DICT
    textos['top'] = topics
    textos['NP1'] = repNP1  
    textos['NP2'] = repNP2
    textos['NT1'] = repNT1
    textos['PERS'] = repPERS
    textos['EMP'] = repEMP
    textos['NT2'] = repNT2     
    
    return textos

def dict_textos2():    
    textos = {}    
    #REPLYS
    repNP   = ('Muchas gracias por su tiempo. Vamos a analizar y nos ponemos en contacto con usted.') 
    repPP   = ('Por ahora no mas analisis.')
    
    #FILL DICT
    textos['NP'] = repNP  
    textos['PP'] = repPP   
    
    return textos
    
    
def dict_topics():
    #Greeting?
    greeting_tokens = ["hello", "hi", "greetings", "good", "morning"]
    
    #Topic tokens
    tokens_estudio_jp = ['actuarial', 'employee', 'employer', 'company', 'retirement', 'labor', 'liabilities']
    tokens_consultoria = ['technical', 'note', 'insurance', 'prepaid', 'medicine', 'consulting', 'consult', 'consultancy',
                      'company', 'statistical', 'mathematical', 'math', 'analysis']
    tokens_rrhh = ['salary', 'level', 'compensation', 'wage', 'climate']
    tokens_iess = ['retirement', 'iess', 'disability', 'old', 'age', 'death', 'insurance']
    tokens_jobseeker = ['hiring', 'hire']    
       
    topics = {}
    topics['gt'] = greeting_tokens
    topics['jp'] = tokens_estudio_jp 
    topics['c'] = tokens_consultoria          
    topics['rrhh'] = tokens_rrhh
    topics['iess'] = tokens_iess
    topics['js'] = tokens_jobseeker    
    
    return topics




def proc_message(message, context): 
    
    if context[0] == 0: #ESTADO 0        
        topic_l = np.array([0,0,0,0,0]) #0: jub-pat, 1: consultoria, 2: RRHH, 3: IESS, 4: JOB SEEKERS
        topics = dict_topics() 
        textos = dict_textos0()
        gt = 0
        ret_message = ''
        
        try:        
            #TRANSLATE AND SENTIMENT ANALYSIS   
            blob = TextBlob(message)
            
            if blob.detect_language() != 'en':
                blob = blob.translate(to='en').lower() 
            else:
                blob = blob.lower()            
            
            pol = blob.sentiment[0]
            
            #TOPIC ANALYSIS  
            for w in blob.words:
                w1 = w.lemmatize() ; w2 = w
                if (w1 in topics['gt']) or (w2 in topics['gt']):
                    gt += 1         
                if (w1 in topics['jp']) or (w2 in topics['jp']):
                    topic_l[0] += 1
                if (w1 in topics['c']) or (w2 in topics['c']):
                    topic_l[1] += 1
                if (w1 in topics['rrhh']) or (w2 in topics['rrhh']):   
                    topic_l[2] += 1
                if (w1 in topics['iess']) or (w2 in topics['iess']):    
                    topic_l[3] += 1
                if (w1 in topics['js']) or (w2 in topics['js']):   
                    topic_l[4] += 1    
        
            a  = np.argmax(topic_l) #a says what topic is the text, independent of gt  that says if we have a greeting
            
            
            #ASSIGN REPLY  (pol, gt, topic_l)         
            if pol < -0.05:                                 #negative polarity (0.05 based on tests, maybe modify it)                
                ret_message = textos['NP']
                context = [1, a, 'NP', blob]                #Migra a estado 1, NP
                
            else:
                if max(topic_l) > 0:                          #if there is a topic found
                    if a < 4:                                 #not job seeker
                        ret_message = textos['RT'].format(textos['top'][a])
                        context = [1, a, 'PP', blob]         #Migra a estado 1, PP
                        
                    else:                                     #job seeker
                        ret_message = textos['JS']
                        context = [0, None, None, None]                 
                    
                elif gt > 0:
                    ret_message = textos['GT']
                    context = [0, None, None, None] 
                    
                    
                else: #Not understood        
                    ret_message = textos['NT']
                    context = [0, None, None, None] 
        
        except:   
            ret_message = textos['NT']
            context = [0, None, None, None]  
        
        
    elif context[0] == 1: #ESTADO 1
        textos = dict_textos1()
        
        if context[2] == 'NP':            #Negative polarity
            try:
                message = message.lower()
                
                if message == 'si':        #Quiere presentar una queja formal
                    ret_message = textos['NP1']
                    context = [2, context[1], 'NP', context[2]]   #Migra a estado 2
                
                elif message == 'no':                     #No
                    ret_message = textos['NP2']
                    context = [0, None, None, None]
                
                else:                                    #user enters other thing (resp No entendi)
                    ret_message = textos['NT1']
                    context = [1, context[1], 'NP', context[2]]
            
            except:                                      #other errors (resp No entendi)
                ret_message = textos['NT1']
                context = [1, context[1], 'NP', context[2]]  #migrate back to same state
        
        else:                           #Positive polarity
            try:
                message = message.lower()
                
                if message == 'persona natural':    #a nombre de persona natural o empresa?
                    ret_message = textos['PERS'].format(textos['top'][context[1]])
                    context = [0, None, None, None]  
                    
                elif message == 'empresa':
                    ret_message = textos['EMP']
                    context =  [2, context[1], 'PP', context[2]]     #Migra a estado 2             
                
                else:     #No entendi
                    ret_message = textos['NT2'].format(textos['top'][context[1]])
                    context = [1, context[1], 'PP', context[2]]  #migrate back to same state                      
                    
            except:    #Algun error en el ingreso
                ret_message = textos['NT2'].format(textos['top'][context[1]])
                context = [1, context[1], 'PP', context[2]]  #migrate back to same state 
                
        
    else:  #ESTADO 2
        textos = dict_textos2()
        
        if context[2] == 'NP':            #Negative polarity
            ret_message = textos['NP']
            context =  [0, None, None, None] 
            
        else:                           #Positive polarity
            ret_message = textos['PP']
            context =  [0, None, None, None] 
                    
    
    return ret_message, context