# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 17:15:56 2019

@author: rober
"""

from flask import Flask, request
import requests
from json import dumps
from collections import defaultdict
from text_processer import proc_message


class ChatraException(Exception):
    pass



class ChatraClient():
    # Initilizing
    def __init__(self, headers):
        self.base_api = "https://app.chatra.io/api"
        self.agent_id = "XXX"    #we only have one agent (daniela)
        self.headers = headers
        self.users_dict = defaultdict(lambda: [0, None, None, None, None, 0, None, None, None]) 
        self.test_users = ["XXX"]        
   

    @classmethod
    def token_authentication(cls, api_key, api_secret):
        return cls({
            "Content-Type": "application/json",
            "Authorization": "Chatra.Simple %s:%s" % (api_key, api_secret)

        })
    
    def handle(self, payload):   
        if payload.get('messages'):
            for m in payload.get('messages'):
                if m['type'] == "client":   #we only respond to client messages for now (not agents)
                    if m['message']:
                        self.parse_message(payload.get('eventName'), m['message'], payload.get('client')['id'])
                    
                    
    def parse_message(self, eventName, message, client_id):
        print(eventName)
        print(message)
        print(client_id)              #we print info of people who communicate with chat (testing phase)
        
        if eventName == 'chatStarted' or eventName == 'chatFragment':        
            context = self.users_dict[client_id]   #context for chat
            out_message, context = proc_message(message, context, client_id)
            if client_id in self.test_users:   #only respond to test users (testing phase)
                self.send_message(client_id, out_message, self.agent_id) 
            self.users_dict[client_id] = context
        
        
    def send_message(self, client_id, text, agent_id):
        payload = {"clientId": client_id, "text": text, "agentId": agent_id}        

        return self.post("/messages/", data=payload)
    
    # Request Methods
    def post(self, url, data, **kwargs):
        return self.request("post", url, data=dumps(data), **kwargs)
    

    # Actual Request call & Headers
    def request(self,method, url,**kwargs):
        kwargs['headers'] = self.headers
        url = "".join([self.base_api, url])
        response = requests.request(method,url, **kwargs)
        if response.status_code == 200:
            return response.json()
        else:
            raise ChatraException(response.content)
        
            
    
    
    
chatra = ChatraClient.token_authentication("XXX","XXX")

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
       chatra.handle(request.get_json())
    return ''


if __name__ == '__main__':
    app.run()
