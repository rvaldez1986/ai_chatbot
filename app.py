# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 21:17:17 2019

@author: rober
"""

import random
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = 'EAAfYg8rcb0UBAANiWP6trPMhiRh5tAUSOPapdpSmeNP0x2HZAdpjsyKIFm4y31sk9xWcxfyZBHsIUeGyr4oBjwO1SruZAmdWnFqfYh62GZAzwGkFneBRU5rifYnkzlWZAZA97GkM3ehDKgU5vuWB3ixaZB6WWvZAI0rBkpdC2QRfggZDZD'
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


#chooses a random message to send to the user
def proc_message(message):
    if message == 'hola':
        sample_responses = ["hola soy un chatbot con ai"]
    else:
        sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    # return selected item to the user
    return random.choice(sample_responses)   



if __name__ == "__main__":
    app.run()