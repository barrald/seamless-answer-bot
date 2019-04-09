## Seamless Answer Bot

This code is intended to facilitate delivery of a Seamless order to an office by:
* Using the Twilio API to answer a phone call with whatever text specified
* Texting the user that their food has arrived

In the purely notional example here, the bot tells the delivery person to just leave their food on a table on 4, which might hypothetically be a place where food should be left.

In order to use, you will need a Twilio API sid and token, virtual phone number ('from_number'), and a target phone number ('to_number'). The code is meant to be deployed to Heroku using the Procfile, with the API information and phone numbers set using config vars.
