import time
from time import strftime
import RPi.GPIO as io
import datetime
from twilio.rest import TwilioRestClient
from datetime import datetime

ACCOUNT_SID = "A...."
AUTH_TOKEN = "B...."

io.setmode(io.BCM)
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

#pir_pin = 18
door_pin = 23

#io.setup(pir_pin, io.IN)
io.setup(door_pin, io.IN, pull_up_down = io.PUD_UP)

while True:
	#if io.input(pir_pin):
	#	print("PIR ALARM!" + str(datetime.now()))
	if io.input(door_pin):
		local_time = strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
		print("Mailbox has been opened on " + local_time)
		client.messages.create(to="+1570....",
			from_="+1614....",
			body="Hello Master, this is your slave Mail Box. Mail has been delivered on "+ local_time + "!")
		time.sleep(30) #wait for mailman to deliver your mail :-)

	time.sleep(0.5)

