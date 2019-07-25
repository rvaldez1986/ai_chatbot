# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 13:34:15 2019

@author: rober
"""

########### Python 3.6 #############
import requests

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '55c4f6fd25a84e81bc2369845f18f9bf',
}

params ={
    # Query parameter
    'q': 'Quien es el consultor que esta trabajando en mi estudio de jubilacion patronal?',
    # Optional request parameters, set to default values
    'timezoneOffset': '-360',
    'verbose': 'true',
    'spellCheck': 'false',
    'staging': 'false',
}


try:
    r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/d8bd8e1e-7a79-4a00-aa99-4fbc8b1a8425',headers=headers, params=params)
    print(r.json())

except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################