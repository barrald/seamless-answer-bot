from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

to_number = os.environ.get('to_number')
from_number = os.environ.get('from_number')

account_sid = os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')

client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
	message = client.messages \
				.create(
					body="Your food is here",
					from_= from_number,
					to= to_number
				)

	print(message.sid)

	resp = VoiceResponse()

	resp.say("Hi, please leave the food on the table on four, thanks!", voice='male', loop=3)

	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)
