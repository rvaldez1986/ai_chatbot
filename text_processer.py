# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:29:38 2019

@author: rober
"""

import nlp_functions as nlp
import textos as txts

    
#context = [Estado: 0, Topic: NA, Polarity: NA, OM: NA, Intent: NA, Counter: 0, RUC:NA, Numproc:NA, Tipo: NA]   

def proc_message(message, context, client_id): 
    
    ST = ['Jubilacion Patronal', 'Consultoria', 'Renuncia/Despido/Desahucio', 'IESS', 'Otros servicios']
    
    if context[0] == 0: #ESTADO 0        
        textos = txts.dict_textos0()  
        dict_palabras = textos["palabras"]
        
        try:    
            pred_topic, pol, OM = nlp.predict_topic(message)            
            
            #ASSIGN REPLY  (in terms of predicted topic)                
            if pred_topic[:2] == 'U:': #unsure
                
                if pred_topic[:6] == 'U: 1T:': #unsure 1 topic 'U: 1T: T0'
                    T0 = pred_topic[7:]
                    ret_message = textos["U1T"].format(T0)
                    context = [0.5, pred_topic, pol, OM, None, context[5]+1, None, None, None]      #Migra a estado 0.5                    
                    
                    
                elif pred_topic[:6] == 'U: 2T:': #unsure 2 topics 'U: 2T: T0, T1'
                    b = pred_topic[7:].index(','); T0 = pred_topic[7:7+b]; T1 = pred_topic[7+b+2:]
                    ret_message = textos["U2T"].format(T0, T1)
                    context = [0.5, pred_topic, pol, OM, None, context[5]+1, None, None, None]      #Migra a estado 0.5
                    
                
                else:  #unsure no topic 'U: No Topic 'U: NT: T0'
                    T0 = pred_topic[7:]
                    ret_message = textos["UNT"].format(T0, dict_palabras[T0])
                    context = [0.5, pred_topic, pol, OM, None, context[5]+1, None, None, None]      #Migra a estado 0.5                 
                    
            else: #topic found             
                ret_message, context = nlp.assign_response0p5(ST, pred_topic, pol, OM, context, textos)              
        
        except Exception as e:   
            ret_message = textos['CE']
            context = [0, None, None, None, None, 0, None, None, None]
            print('Exception en proc_message: {0}'.format(e))
          
    
    elif context[0] == 0.5: #ESTADO 0.5 unsure
        textos = txts.dict_textos0()  #we use the same as in previous section
        dict_palabras = textos["palabras"]
        pred_topic = context[1]; pol = context[2]; OM = context[3]; counter = context[5]
        
        if counter < 3:        
            if pred_topic[:6] == 'U: 1T:': #unsure 1 topic 'U: 1T: T0'
                T0 = pred_topic[7:]
                res = nlp.proc_messageYN(message)
            
                if res == 'si':
                    ret_message, context = nlp.assign_response0p5(ST, T0, pol, OM, context, textos)
                else:                
                    ret_message = textos["UNT"].format('IESS', dict_palabras['IESS'])  #se da el iess como ejemplo porque T0 no es
                    context = [0.5, 'U: NT: IESS', pol, OM, None, context[5]+1, None, None, None]  #migra como unsure no topic!
                    
            elif pred_topic[:6] == 'U: 2T:': #unsure 2 topics 'U: 2T: T0, T1'
                b = pred_topic[7:].index(','); T0 = pred_topic[7:7+b]; T1 = pred_topic[7+b+2:]
                res = nlp.proc_messagep51(message, T0, T1)  #this will sort out topic
                ret_message, context = nlp.assign_response0p5(ST, res, pol, OM, context, textos)        
                    
            else:  #unsure no topic 'U: NT'            
                pred_topic2, pol2, OM2 = nlp.predict_topic(message)                             
                
                if pred_topic2 not in ['Hi Five', 'Greeting', 'No Topic'] and pred_topic2[:2] != 'U:':
                    ret_message, context = nlp.assign_response0p5(ST, pred_topic2, pol2, OM2, context, textos)                
                else:
                    ret_message, context = nlp.assign_response0p5(ST, 'No Topic', pol2, OM2, context, textos)  #moves to no topic        
        
        else:  #loop 3 or more times
            ret_message = textos['CE']
            context = [0, None, None, None, None, 0, None, None, None]     
            
        
        
    elif context[0] == 1: #ESTADO 1
        textos = txts.dict_textos1()       
        
        if context[1] in ST:            
            res = nlp.proc_message1ST(message)            

            if res == "persona":                
                url_sug = nlp.suggest_url(context[3], context[1])
                
                
                if url_sug and context[1]=='IESS':
                    ret_message = textos["ST"][5].format(context[1], url_sug)
                    context = [2, context[1], context[2], context[3], None, context[5]+1, None, None, "persona"]
                elif url_sug:
                    ret_message = textos["ST"][0].format(context[1], url_sug)
                    context = [0, None, None, None, None, 0, None, None, None] 
                else:
                    ret_message = textos["ST"][1].format(context[1])                 
                    context = [0, None, None, None, None, 0, None, None, None]                  

            elif res == "empresa":
                ret_message = textos["ST"][2]           #list in dictionary (ST has 3 messages)
                context = [2, context[1], context[2], context[3], None, context[5]+1, None, None, "empresa"]
                
            elif res == "salir":
                ret_message =  textos['salir']         #list in dictionary (ST has 3 messages)
                context = [0, None, None, None, None, 0, None, None, None]

            else:
                if context[5] < 2:
                    ret_message = textos["ST"][3].format(context[1])           #list in dictionary (ST has 3 messages)
                    context = [1, context[1], context[2], context[3], None, context[5]+1, None, None, None]
                else:
                    ret_message = textos["ST"][4]       
                    context = [0, None, None, None, None, 0, None, None, None]
                    

        elif context[1] == "Queja":
            res = nlp.proc_messageYN(message)            
            if res == "si":
                ret_message = textos["Queja"][0]           
                context = [2, context[1], context[2], context[3], None, context[5]+1, None, None]
            elif res == "no":
                ret_message = textos["Queja"][1]             
                context = [0, None, None, None, None, 0, None, None, None] 
            
            elif res == "salir":
                ret_message =  textos['salir']         #list in dictionary (ST has 3 messages)
                context = [0, None, None, None, None, 0, None, None, None]      
            
            else:
                if context[5] < 2:
                    ret_message = textos["Queja"][2]            
                    context = [1, context[1], context[2], context[3], None, context[5]+1, None, None, None]
                else:
                    ret_message = textos["ST"][4]       
                    context = [0, None, None, None, None, 0, None, None, None]
            
        else: #context[1] == "NT":
            res = nlp.proc_message1NT(message)
            
            if res == "actuaria":
                ret_message = textos["NT"][0]              
                message2 = textos["NT"][1].format(client_id, context[3]).encode("utf-8")             
                toaddr = "sebastian.tamayo@actuaria.com.ec"  #por ahora mi correo
                ret = nlp.send_email(message2, toaddr)           
                context = [0, None, None, None, None, 0, None, None, None] 
                
            elif res == "otro":                
                ret_message = nlp.proc_wiki(context[3])                    
                context = [0, None, None, None, None, 0, None, None, None] 
                
            elif res == "salir":
                ret_message =  textos['salir']         #list in dictionary (ST has 3 messages)
                context = [0, None, None, None, None, 0, None, None, None] 
                
            else:
                if context[5] < 2:
                    ret_message = textos["NT"][2]            
                    context = [1, context[1], context[2], context[3], None, context[5]+1, None, None, None]
                else:
                    ret_message = textos["ST"][4]       
                    context = [0, None, None, None, None, 0, None, None, None]
        
    
    
    elif context[0] == 2:  #ESTADO 2
        textos = txts.dict_textos2()       
        
        if context[1] in ST:    #empresa ST   
            
            if context[8] == "empresa":
            
                res = nlp.proc_message2ST(message)            
                
                if res not in ['na','salir']:     #ruc encontrado                                 
                    try:    
                        topIn, entities = nlp.azure_q1(context[3])
                        
                        if topIn == 'reqCotizacion':
                            ret_message = textos["ST"][0]            
                            context = [3, context[1], context[2], context[3], topIn, context[5]+1, res, None, None]
                            
                        elif topIn == 'reqCurrProcInfo':
                            ret_message = textos["ST"][1]            
                            context = [3, context[1], context[2], context[3], topIn, context[5]+1, res, None, None]   
                            
                        elif topIn == 'reqTiempo':
                            ret_message = textos["ST"][2]              
                            context = [3, context[1], context[2], context[3], topIn, context[5]+1, res, None, None]   
                        
                        else:    #None Intent from azure                        
                            url_sug = nlp.suggest_url(context[3], context[1])
                            
                            if url_sug:                        
                                 ret_message = textos["ST"][3].format(url_sug)                          
                            else:
                                ret_message = textos["ST"][4]      
                            
                            message2 = textos['interno'].format(client_id, context[3]).encode("utf-8")             
                            toaddr = "sebastian.tamayo@actuaria.com.ec"  #por ahora mi correo
                            ret = nlp.send_email(message2, toaddr)
                            context = [0, None, None, None, None, 0, res, None, None]
                            
                            
                    except Exception as e:  #Error                    
                        ret_message = textos["ST"][4]     
                        context = [0, None, None, None, None, 0, res, None, None]
                        
                        message2 = textos['interno'].format(client_id, context[3]).encode("utf-8")             
                        toaddr = "sebastian.tamayo@actuaria.com.ec"  #por ahora mi correo
                        ret = nlp.send_email(message2, toaddr)                   
                        
                        print('Exception en communication with azure q1: {0}'.format(e))

                elif res == "salir":
                    ret_message =  textos['salir']         
                    context = [0, None, None, None, None, 0, None, None, None]                
                    
                else:   #no se entendio ingreso de RUC             
                    if context[5] < 3:
                        ret_message = textos["ST"][5]   #puede repetir, ingrese su ruc           
                        context = [2, context[1], context[2], context[3], None, context[5]+1, None, None, None]
                    else:
                        ret_message = textos["ST"][6]            
                        context = [0, None, None, None, None, 0, None, None, None]           
            
            else:  #Persona
                res = nlp.proc_messageYN(message)            
                if res == "si":
                    ret_message = textos["PN"][0].format(context[1])           
                    context = [4, context[1], context[2], context[3],'reqCotizacion', context[5]+1, None, None,context[8]]
                elif res == "no":
                    ret_message = textos["PN"][1]             
                    context = [0, None, None, None, None, 0, None, None, None] 
                else:
                    if context[5] < 3:
                        ret_message = textos["PN"][2]   
                        context = [2, context[1], context[2], context[3], None, context[5]+1, None, None, context[8]]
                    else:
                        ret_message = textos["PN"][3]   
                        context = [0, None, None, None, None, 0, None, None, None] 
               
                
        else:  #Queja
            message2 = textos["MSG"][0].format(message, context[3]).encode('utf-8')        
            toaddr = "sebastian.tamayo@actuaria.com.ec"  #por ahora mi correo
            ret = nlp.send_email(message2, toaddr)
                    
            ret_message = textos["MSG"][1]
            
            context = [0, None, None, None, None, 0, None, None, None]   
            

    
    elif context[0] == 3:  #ESTADO 3
        textos = txts.dict_textos3() 
        res = nlp.proc_messageYN(message)  
        
          
        if res == "si":            
            if context[4] == 'reqCotizacion':
                ret_message = textos["ST"][0].format(context[1])          
                context = [4, context[1], context[2], context[3], context[4], context[5]+1,context[6], None, None]
                
            elif context[4] == 'reqTiempo':
                ret_message = textos["ST"][1].format(context[1])   
                context = [0, None, None, None, None, 0, None, None, None]  
            
            
            else:
                try:
                    razon_social, codigo_cliente = nlp.consulta_ruc(context[6]) #currProcessInfo
                
                    if nlp.consulta_ruc(context[6])!="None":  
                        ret_message = textos["KO"][0].format(razon_social)       
                        context = [4, context[1], context[2], context[3], context[4], context[5]+1, context[6], None, None]
                
                except Exception:
                    ret_message=textos["KO"][1]
                    context = [0, None, None, None, None, 0, None, None, None]
        
        elif res == "no":
            ret_message = textos["KO"][2]             
            message2 = textos["KO"][3].format(client_id, context[3]).encode("utf-8")             
            toaddr = "sebastian.tamayo@actuaria.com.ec"  #por ahora mi correo
            ret = nlp.send_email(message2, toaddr)            
            
            context = [0, None, None, None, None, 0, None, None, None]
            
        
        elif res == "salir":
            ret_message =  textos['salir']         #list in dictionary (ST has 3 messages)
            context = [0, None, None, None, None, 0, None, None, None]     
        
        
        else:  #answer (yes/no) not understood
            if context[4] == 'reqCotizacion':
                ret_message = textos["ST"][2]             
            else:
                ret_message = textos["ST"][3]    
            
            context = [3, context[1], context[2], context[3], context[4], context[5]+1, None, None, None]  #independiente del intent vuelve a 3
        
        
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
            
            context = [0, None, None, None, None, 0, None, None, None]  
        

        else:  #current_process_info: 
            res = nlp.proc_message_pro(message)
            
            if res != 'na':
                context = [4, context[1], context[2], context[3], context[4], context[5]+1, context[6], res, None]   
            
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
                        
                        
                        context = [0, None, None, None, None, 0, None, None, None]

                    
                    else: 
                        ret_message = textos['KO'][1]
                        context = [0, None, None, None, None, 0, None, None, None]
                        
                except Exception as b:   
                        ret_message = textos['KO'][1]
                        context = [0, None, None, None, None, 0, None, None, None]
                        print('Exception en comunicacion con Kohinor: {0}'.format(b))  
            else:
                        ret_message = textos['KO'][2]             
                        context = [4, context[1], context[2], context[3], context[4], context[5]+1, context[6], None, None]
                       
    
    else:  #ESTADO 5
        textos = txts.dict_textos5() 
        ret_message = textos["ST"]            
        context = [0, None, None, None, None, 0, None, None, None]     

        
    
    return ret_message, context

