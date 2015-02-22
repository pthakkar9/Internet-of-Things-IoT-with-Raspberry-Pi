import time
import RPi.GPIO as io
import datetime
from twilio.rest import TwilioRestClient
from datetime import datetime

ACCOUNT_SID = "6..."
AUTH_TOKEN = "4..."

io.setmode(io.BCM)
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

pir_pin = 18
door_pin = 23

io.setup(pir_pin, io.IN)
io.setup(door_pin, io.IN, pull_up_down = io.PUD_UP)

while True:
	if io.input(pir_pin):
		print("PIR ALARM!" + str(datetime.now()))
	if io.input(door_pin):
		print("DOOR ALARM!" + str(datetime.now()))
		client.messages.create(to="+1570...",
			from_="+1614...",
			body="Hello Master, this is your Mail Box. Mail has been delivered on "+ str(datetime.now()) + "!")
		time.sleep(30) #wait for mailman to deliver your mail :-)

	time.sleep(0.5)

