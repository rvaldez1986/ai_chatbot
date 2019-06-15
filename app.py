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

from flask import Flask, request
from pymessenger.bot import Bot
from text_processer import proc_message

app = Flask(__name__)
ACCESS_TOKEN = 'EAAfYg8rcb0UBADZBoT3NnDvUTO6cEzBsjycuC96YWfn5KhjN8Bp8slgwLYdw298keZATXQpS6nQo88lO34zgHgim7KNLzk03WT66Tk5lLpIg695NKPi6FzOf0LJwZAwhcfSjZCk2KHyH1IVdcl1jAxkvUyo7xwZCFyzpuVwrP8gZDZD'
VERIFY_TOKEN = 'VERIFY_TOKEN'
bot = Bot(ACCESS_TOKEN)

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
                    out_message = proc_message(in_message)
                    bot.send_text_message(recipient_id, out_message)
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