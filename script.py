import serial 
import json
import requests
from datetime import datetime

device = 'COM8'
arduino = serial.Serial(device, 9600)

while(1):
	data = arduino.readline()
	data = data.split(" ")

	data1 = data[0]
	data2 = data[1]

	refparking = data1[0:4]	
	
	reference1 = int(data1[4:7],2)
	state1 = data1[7:8]
	
	reference2 = int(data2[4:7],2)
	state2 = data2[7:8]
	print refparking
	print reference1
	print state1
	print reference2
	print state2

	time = str(datetime.now())
	time = time[:19]

	url = 'http://ensismartpark.000webhostapp.com/login_register/consumer.php'
	payload = {"sensor_ref1":reference1,"state1":state1,"ref_parking":refparking,"sensor_ref2":reference2,"state2":state2,"lastupdate":time}
	
	response = requests.post(url, data=dict(payload=json.dumps(payload)))
	print response
