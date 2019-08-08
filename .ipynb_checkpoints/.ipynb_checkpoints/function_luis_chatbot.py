# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 15:07:36 2019

@author: rober
"""


import requests

def f(texto):   
    
    params ={
    # Query parameter
    'q': texto,
    # Optional request parameters, set to default values
    'timezoneOffset': '-360',
    'verbose': 'true',
    'spellCheck': 'false',
    'staging': 'false',
    }
    
    headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '55c4f6fd25a84e81bc2369845f18f9bf',
    }
    
    try:
        r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/d8bd8e1e-7a79-4a00-aa99-4fbc8b1a8425',headers=headers, params=params)
        data = r.json()
        intents = data.get('intents')
        intents[1].get('intent')

    except Exception as e:
        pass