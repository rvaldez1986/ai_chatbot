# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:29:38 2019

@author: rober
"""

import nlp_functions as nlp
import textos as txts

    
#context = [Estado: 0, Topic: NA, Polarity: NA, OM: NA, Intent: NA, Counter: 0, RUC:NA, Numproc:NA]   

def proc_message(message, context): 
    
    ST = ['Jubilacion Patronal', 'Consultoria', 'Renuncia/Despido/Desahucio', 'IESS', 'Otros servicios']
    
    if context[0] == 0: #ESTADO 0        
        textos = txts.dict_textos0()
        ret_message = ''
        
        try:    
            pred_topic, pol, OM = nlp.predict_topic(message)
            
            #ASSIGN REPLY  (in terms of predicted topic)           
            
            if pred_topic in ST:
                ret_message = textos["ST"].format(pred_topic)
                context = [1, pred_topic, pol, OM, None, context[5]+1, None, None]      #Migra a estado 1
            
            elif pred_topic == "Queja":                                              
                ret_message = textos["Queja"]
                context = [1, pred_topic, pol, OM, None, context[5]+1, None, None]                
                
            elif pred_topic == "Hi Five":
                ret_message = textos["Hi Five"]
                context = [0, None, None, None, None, 0, None, None] 

            elif pred_topic == "job seeker":
                ret_message = textos["job seeker"]
                context = [0, None, None, None, None, 0, None, None]
                
            elif pred_topic == "Contacto":
                ret_message = textos["Contacto"]
                context = [0, None, None, None, None, 0, None, None]
                
            elif pred_topic == "Greeting":
                ret_message = textos["Greeting"]
                context = [0, None, None, None, None, 0, None, None]
                
            elif pred_topic == 'Charlas/Capacitaciones':
                ret_message = textos['Charlas/Capacitaciones']
                context = [0, None, None, None, None, 0, None, None]
                
            elif pred_topic == 'Facturacion/Retencion/Cobros':
                ret_message = textos['Facturacion/Retencion/Cobros']
                context = [0, None, None, None, None, 0, None, None]                 
            else:
                ret_message = textos['NT']           #No topic, could be wikipedia
                context = [1, 'NT', None, OM, None, context[5]+1, None, None]              
        
        except Exception as e:   
            ret_message = textos['CE']
            context = [0, None, None, None, None, 0, None, None]
            print(e)
          

        
        
    elif context[0] == 1: #ESTADO 1
        textos = txts.dict_textos1()       
        
        if context[1] in ST:            
            res = nlp.proc_message1ST(message)            

            if res == "persona":                
                url_sug = nlp.suggest_url(context[3], context[1])
                if url_sug:
                    ret_message = textos["ST"][0].format(context[1], url_sug)          
                else:
                    ret_message = textos["ST"][1].format(context[1]) 
                
                context = [0, None, None, None, None, 0, None, None]              
                

            elif res == "empresa":

                ret_message = textos["ST"][2]           #list in dictionary (ST has 3 messages)
                context = [2, context[1], context[2], context[3], None, context[5]+1, None, None]

            else:

                ret_message = textos["ST"][3].format(context[1])           #list in dictionary (ST has 3 messages)
                context = [1, context[1], context[2], context[3], None, context[5]+1, None, None]

        elif context[1] == "Queja":
            res = nlp.proc_messageYN(message)            
            if res == "si":
                ret_message = textos["Queja"][0]           
                context = [2, context[1], context[2], context[3], None, context[5]+1, None, None]
            elif res == "no":
                ret_message = textos["Queja"][1]             
                context = [0, None, None, None, None, 0, None, None] 
            else:
                ret_message = textos["Queja"][2]            
                context = [1, context[1], context[2], context[3], None, context[5]+1, None, None]
            
        elif context[1] == "NT":
            res = nlp.proc_message1NT(message)
            if res == "actuaria":
                ret_message = textos["NT"][0]           
                context = [0, None, None, None, None, 0, None, None] 
            elif res == "otro":                
                ret_message = nlp.proc_wiki(context[3])          
                context = [0, None, None, None, None, 0, None, None] 
            else:
                ret_message = textos["NT"][1]            
                context = [1, context[1], context[2], context[3], None, context[5]+1,None,None]
                
        
    
    
    elif context[0] == 2:  #ESTADO 2
        textos = txts.dict_textos2()       
        
        if context[1] in ST:            
            res = nlp.proc_message2ST(message)
            
            if res != 'na':#ruc encontrado                
                topIn, entities = nlp.azure_q1(context[3])                
                try:             
                    if topIn == 'reqCotizacion':
                        ret_message = textos["ST"][0]            
                        context = [3, context[1], context[2], context[3], topIn, context[5]+1, res, None]
                    elif topIn == 'reqCurrProcInfo':
                        print(res,topIn)
                        ret_message = textos["ST"][1]            
                        context = [3, context[1], context[2], context[3], topIn, context[5]+1, res, None]   
                    else:    #None Intent
                        ret_message = textos["ST"][2]            
                        context = [0, None, None, None, None, 0, res, None]
                        
                except Exception:  #Error
                    ret_message = textos["ST"][2]            
                    context = [0, None, None, None, None, 0, res, None]
            else:
                ret_message = textos["ST"][3]   #puede repetir, ingrese su ruc           
                context = [2, context[1], context[2], context[3], None, context[5]+1, None, None]
        else:
            message2 = textos["MSG"][0].format(message, context[3]).encode('utf-8')        
            toaddr = "sebastian.tamayo@actuaria.com.ec"  #por ahora mi correo
            ret = nlp.send_email(message2, toaddr)
                    
            if ret == 'success':        
                ret_message = textos["MSG"][1]
            else:
                ret_message = textos["MSG"][2]
            context = [0, None, None, None, None, 0, None, None]   
            

    
    elif context[0] == 3:  #ESTADO 3
        textos = txts.dict_textos3() 
        res = nlp.proc_messageYN(message)  
          
        if res == "si":            
            if context[4] == 'reqCotizacion':
                ret_message = textos["ST"][0].format(context[1])          
                context = [4, context[1], context[2], context[3], context[4], context[5]+1,context[6],None]
            
            else:
                try:
                    razon_social, codigo_cliente = nlp.consulta_ruc(context[6]) #currProcessInfo
                
                    if nlp.consulta_ruc(context[6])!="None":  
                        ret_message = textos["KO"][0].format(razon_social)       
                        context = [4, context[1], context[2], context[3], context[4], context[5]+1, context[6], None]
                
                except Exception:
                    ret_message=textos["KO"][1]
                    context = [0, None, None, None, None, 0, None, None]
        
        elif res == "no":
            ret_message = textos["KO"][2]             
            context = [0, None, None, None, None, 0, None, None]
            
        else:  #answer (yes/no) not understood
            if context[4] == 'reqCotizacion':
                ret_message = textos["ST"][1]             
            else:
                ret_message = textos["ST"][2]    
            
            context = [3, context[1], context[2], context[3], context[4], context[5]+1, None, None]  #independiente del intent vuelve a 3
        
        
    elif context[0] == 4:
        textos = txts.dict_textos4()         
        
        if context[4] == 'reqCotizacion':
            message2 = textos["MSG"][0].format(message).encode('utf-8')        
        
            toaddr = "sebastian.tamayo@actuaria.com.ec"  #por ahora mi correo
            ret = nlp.send_email(message2, toaddr)
        
            if ret == 'success':        
                ret_message = textos["MSG"][1]
            else:
                ret_message = textos["MSG"][2]
            
            context = [0, None, None, None, None, 0, None, None]  
        

        else:  #current_process_info: 
            res = nlp.proc_message_pro(message)
            
            if res != 'na':
                context = [4, context[1], context[2], context[3], context[4], context[5]+1, context[6], res]   
            
                try:                
                    nombre_encargado,Extension_encargado,correo_electronico,estado_proceso,codigo_cliente_proc = nlp.consulta_proc(context[7])
                    razon_social,codigoCliente = nlp.consulta_ruc(context[6])
                    
                    if  nlp.consulta_proc(context[7])!="None" and codigo_cliente_proc==codigoCliente:  
                        ret_message = textos["KO"][0].format(razon_social,estado_proceso,nombre_encargado,correo_electronico,Extension_encargado,codigo_cliente_proc)       
                        
                        message2 = textos["KO"][3].format(message,context[3],razon_social,estado_proceso,codigo_cliente_proc).encode('utf-8')        
                        toaddr="sebastian.tamayo@actuaria.com.ec"  #por ahora mi correo
                        ret = nlp.send_email(message2, toaddr)
                        if ret == 'success':        
                            ret_message = textos["KO"][0].format(razon_social,estado_proceso,nombre_encargado,correo_electronico,Extension_encargado,codigo_cliente_proc)
                        else:
                            ret_message = textos["KO"][0].format(razon_social,estado_proceso,nombre_encargado,correo_electronico,Extension_encargado,codigo_cliente_proc)
                        
                        
                        context = [0, None, None, None, None, 0, None, None]

                    
                    else: 
                        ret_message = textos['KO'][1]
                        context = [0, None, None, None, None, 0, None, None]
                        
                except Exception as b:   
                        ret_message = textos['KO'][1]
                        context = [0, None, None, None, None, 0, None, None]
                        print(b)  
            else:
                        ret_message = textos['KO'][2]             
                        context = [4, context[1], context[2], context[3], context[4], context[5]+1, context[6], None]
                       
    
    else:  #ESTADO 5
        textos = txts.dict_textos5() 
        ret_message = textos["ST"]            
        context = [0, None, None, None, None, 0, None, None]     

        
    
    return ret_message, context

