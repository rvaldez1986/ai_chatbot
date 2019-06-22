# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 13:35:59 2019

@author: rober
"""

import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
    

from flask import Flask, request
from fbmessenger import BaseMessenger
from fbmessenger.thread_settings import GreetingText, GetStartedButton, MessengerProfile
from collections import defaultdict
from text_processer import proc_message
import requests


class Messenger(BaseMessenger):
    def __init__(self, page_access_token, **kwargs):
        super(Messenger, self).__init__(page_access_token)
        self.users_dict = defaultdict(lambda: [0, None, None, None]) 
        
    def handle(self, payload):
        for entry in payload['entry']:
            for message in entry['messaging']:
                if message.get('message'):
                    return self.receive_message(message)
                elif message.get('postback'):
                    return self.postback(message)

    def postback(self, message):
        payload = message['postback']['payload']
        recipient_id = message['sender']['id']
        if 'start' in payload: 
            out_message =  'Hola yo soy su chatbot'
            self.send_text_message(recipient_id, out_message)            
        
    def receive_message(self, message):                 
        #Facebook Messenger ID for user so we know where to send response back to
        recipient_id = message['sender']['id']
        if message['message'].get('text'):
            in_message = message['message']['text']
            context = self.users_dict[recipient_id]
            out_message, context = proc_message(in_message, context)
            self.send_text_message(recipient_id, out_message)
            self.users_dict[recipient_id] = context
        #if user sends us a GIF, photo,video, or any other non-text item
        if message['message'].get('attachments'):
            out_message =  'Gracias por los documentos, los analizaremos y nos contactaremos con usted.'
            self.send_text_message(recipient_id, out_message) 
        return "Message Processed"
    
      
    def send_text_message(self, recipient_id, message, notification_type='REGULAR'):
        """Send text messages to the specified recipient.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/text-message
        Input:
            recipient_id: recipient id to send to
            message: message to send
        Output:
            Response from API as <dict>      """        
        
        payload = {'message': {'text': message}}         
    
        payload['recipient'] = {
            'id': recipient_id
        }
        payload['notification_type'] = notification_type        
     
        request_endpoint = '{0}/me/messages'.format(self.client.graph_url)
        response = requests.post(
            request_endpoint,
            params=self.client.auth_args,
            json=payload
        )
        result = response.json()
        return result
    

    def init_bot(self):
        greeting_text = GreetingText('Welcome to weather bot')
        messenger_profile = MessengerProfile(greetings=[greeting_text])
        messenger.set_messenger_profile(messenger_profile.to_dict())

        get_started = GetStartedButton(payload='start')

        messenger_profile = MessengerProfile(get_started=get_started)
        messenger.set_messenger_profile(messenger_profile.to_dict())


FB_PAGE_TOKEN = ''
FB_VERIFY_TOKEN = 'VERIFY_TOKEN'

app = Flask(__name__)
app.debug = True
messenger = Messenger(FB_PAGE_TOKEN)


@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == FB_VERIFY_TOKEN:
            #messenger.init_bot()
            return request.args.get('hub.challenge')
        raise ValueError('FB_VERIFY_TOKEN does not match.')
    elif request.method == 'POST':
        messenger.handle(request.get_json())
    return ''


if __name__ == '__main__':
    app.run()
    
    
    
#https://www.idiotinside.com/2017/12/22/facebook-messenger-bot-get-started-quick-reply-python/
#https://github.com/rehabstudio/fbmessenger/blob/master/fbmessenger
#https://github.com/davidchua/pymessenger/blob/master/pymessenger/bot.py   
    
    