# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 21:17:17 2019

@author: rober
"""
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from collections import defaultdict
from flask import Flask, request
from pymessenger.bot import Bot
from text_processer import proc_message

users_dict = defaultdict(lambda: [0, None, None, None])

app = Flask(__name__)
ACCESS_TOKEN = 'EAAfYg8rcb0UBAGL9NNwwYoLnrNN28F3xGPZAB4We1aSxmZB3XSdbOThGCk5ZBSJHidP0pb4UoHy8fS9EEVTmn0RqyAVbdcUPvrYxTIjvvAccaMWwEsUoe7QWbZBHpQXUj1EhIaGSsdPn8dWtMX2DZByXwGvEknBHRoZAsDAqjaUwZDZD'
VERIFY_TOKEN = 'VERIFY_TOKEN'
bot = Bot(ACCESS_TOKEN)
#bot.set_greeting_text('Buenos Dias')
#bot.set_get_started_button_payload("HELP")

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot       
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for x in messaging:
            if x.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = x['sender']['id']
                if x['message'].get('text'):
                    in_message = x['message']['text']
                    context = users_dict[recipient_id]
                    out_message, context = proc_message(in_message, context)
                    bot.send_text_message(recipient_id, out_message)
                    users_dict[recipient_id] = context
                #if user sends us a GIF, photo,video, or any other non-text item
                if x['message'].get('attachments'):
                    out_message =  'Gracias por los documentos, los analizaremos y nos contactaremos con usted.'
                    bot.send_text_message(recipient_id, out_message)  
    
    return "Message Processed"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


if __name__ == "__main__":
    app.run()