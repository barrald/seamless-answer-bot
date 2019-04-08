from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

import creds
client = Client(creds.account_sid, creds.auth_token)


app = Flask(__name__)

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
	message = client.messages \
				.create(
					body="Your food is here",
					from_='+15172539971',
					to='+15172904116'
				)

	print(message.sid)

	resp = VoiceResponse()

	resp.say("Hi, please leave the food on the table on four, thanks!", voice='alice', loop=3)

	return str(resp)

@app.route("/", methods=['GET', 'POST'])
def hello():
    return "Hello World!"

if __name__ == "__main__":
	app.run(debug=True)
