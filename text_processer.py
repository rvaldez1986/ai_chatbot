# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:29:38 2019

@author: rober
"""

import nlp_functions as nlp
import textos as txts

    
#ret_message = textos['RT'].format(textos['top'][a])    

def proc_message(message, context): 
    
    ST = ["Jubilacion Patronal", "Renuncia/Despido/Desahucio", "IESS", 
                  "Otros servicios (Charlas/Capacitaciones/Financiera)", "Consultoria"]
    
    if context[0] == 0: #ESTADO 0        
        textos = txts.dict_textos0()
        ret_message = ''
        
        try:    
            pred_topic, pol, OM = nlp.predict_topic(message)
            
            #ASSIGN REPLY  (in terms of predicted topic)           
            
            if pred_topic in ST:
                ret_message = textos["ST"].format(pred_topic)
                context = [1, pred_topic, pol, OM]      #Migra a estado 1
            
            elif pred_topic == "Queja":                                              
                ret_message = textos["Queja"]
                context = [1, pred_topic, pol, OM]                
                
            elif pred_topic == "Hi Five":
                ret_message = textos["Hi Five"]
                context = [0, None, None, None] 

            elif pred_topic == "job seeker":
                ret_message = textos["job seeker"]
                context = [0, None, None, None]
                
            elif pred_topic == "Contacto":
                ret_message = textos["Contacto"]
                context = [0, None, None, None]
                
            elif pred_topic == "Greeting":
                ret_message = textos["Greeting"]
                context = [0, None, None, None]
                
            else:
                ret_message = textos['NT']           #No topic, could be wikipedia
                context = [1, 'NT', None, OM]              
        
        except:   
            ret_message = textos['CE']
            context = [0, None, None, None]  
        
        
    elif context[0] == 1: #ESTADO 1
        textos = txts.dict_textos1()       
        
        if context[1] in ST:            
            res = nlp.proc_message1ST(message)            
            if res == "persona":
                ret_message = textos["ST"][0].format(context[1])           #list in dictionary (ST has 3 messages)
                context = [0, None, None, None]      
            elif res == "empresa":
                ret_message = textos["ST"][1]           #list in dictionary (ST has 3 messages)
                context = [2, context[1], context[2], context[3]]
            else:
                ret_message = textos["ST"][2].format(context[1])           #list in dictionary (ST has 3 messages)
                context = [1, context[1], context[2], context[3]]
                
        elif context[1] == "Queja":
            res = nlp.proc_messageYN(message)            
            if res == "si":
                ret_message = textos["Queja"][0]           
                context = [2, context[1], context[2], context[3]]
            elif res == "no":
                ret_message = textos["Queja"][1]             
                context = [0, None, None, None] 
            else:
                ret_message = textos["Queja"][2]            
                context = [1, context[1], context[2], context[3]]
            
        elif context[1] == "NT":
            res = nlp.proc_message1NT(message)
            if res == "actuaria":
                ret_message = textos["NT"][0]           
                context = [0, None, None, None] 
            elif res == "otro":                
                ret_message = nlp.proc_wiki(context[3])          
                context = [0, None, None, None] 
            else:
                ret_message = textos["NT"][1]            
                context = [1, context[1], context[2], context[3]]
                
        
    elif context[0] == 2:  #ESTADO 2
        textos = txts.dict_textos2()       
        
        if context[1] in ST:            
            res = nlp.proc_message2ST(message) 
            if res != 'na':   #ruc encontrado
                res2 = nlp.algo_clasificador(context[3])
                if res2 == 'Cotizacion':
                    ret_message = textos["ST"][0]            
                    context = [3, context[1], context[2], context[3]]
                else:
                    ret_message = textos["ST"][1]    #no es una cotizacion, por ahora despedida         
                    context = [0, None, None, None]
            else:
                ret_message = textos["ST"][2]   #puede repetir, ingrese su ruc           
                context = [2, context[1], context[2], context[3]]
        else:
            ret_message = textos["Queja"]          
            context = [0, None, None, None]
            
    
    elif context[0] == 3:  #ESTADO 3
        textos = txts.dict_textos3() 
        
        res = nlp.proc_messageYN(message)            
        if res == "si":
            ret_message = textos["ST"][0].format(context[1])          
            context = [4, context[1], context[2], context[3]]
        elif res == "no":
            ret_message = textos["ST"][1]             
            context = [0, None, None, None] 
        else:
            ret_message = textos["ST"][2]            
            context = [3, context[1], context[2], context[3]]
            
    else:  #ESTADO 4
        textos = txts.dict_textos4() 
        
        ret_message = textos["ST"]            
        context = [0, None, None, None]     
        
    
    return ret_message, context