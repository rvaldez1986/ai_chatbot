# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:29:38 2019

@author: rober
"""

def proc_message(message, context): 
    
    if context[0] == 0:
        ret_message = 'Hola'
        context[0] = 1
    else:
        ret_message = 'Ya te salude'
        context[0] = 0
    
    return ret_message, context