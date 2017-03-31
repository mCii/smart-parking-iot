import serial 
import MySQLdb

dbConn = MySQLdb.connect("localhost","root","root","arduino") or die ("could not connect to database");
device = '/dev/ttyACM0'
arduino = serial.Serial(device, 9600)
cursor = dbConn.cursor()
while(1):
	data = arduino.readline()
	dd = data.split()
	reference=dd[0]
	state=dd[1]
	print reference + " ---- " + state	#for testing 
#	cursor.execute("INSERT into sensorState(reference, state) VALUES (%s,%s)", (reference, state)) 
#	cursor.execute(""" 
#		UPDATE sensorState 		#updating the database
#		SET state= %s 
#		WHERE reference = %s"
#	""", (state, reference))
	dbConn.commit()

cursor.close()
