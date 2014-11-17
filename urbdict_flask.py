from flask import Flask, request, redirect, session
import twilio.twiml
from twilio.rest import TwilioRestClient
import unirest
import time
import os

app = Flask(__name__)


def send_reply(query):
    response = unirest.get("https://mashape-community-urban-dictionary.p.mashape.com/define?term={}".format(query),
    headers = {"X-Mashape-Key": "Lji2UqoGLFmshAIy8vGoyrIz6HvEp1pyOjGjsnx0vNXlGzcYtY"}
    )
    try:
        word = response.body['list'][0]['word']
        definition = response.body['list'][0]['definition']
        return word + '\n' + definition
    except:
        return 'Quit making up words, weirdo.'


@app.route("/", methods=['GET', 'POST'])
def smsEcho():
    client = TwilioRestClient()
    clientNumber = request.values.get('From', None)
    clientTextContent = request.values.get('Body', None)
    response = twilio.twiml.Response()
    message = send_reply(clientTextContent)
    response.message(message)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
