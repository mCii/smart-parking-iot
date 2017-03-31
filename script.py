import serial 
import MySQLdb

dbConn = MySQLdb.connect("localhost","root","root","arduino") or die ("could not connect to database");
device = '/dev/ttyACM0'
arduino = serial.Serial(device, 9600)
cursor = dbConn.cursor()
while(1):
	data = arduino.readline()
	dd = data.split()
	reference1 = dd[0]
	state1 = dd[1]
	reference2 = dd[2]
	state2 = dd[3]
	print reference1 + " ---- " + state1 + "/"+ reference2 + "----"+ state2	for testing 
#	cursor.execute("INSERT into sensorState(reference, state) VALUES (%s,%s)", (reference, state)) 
	cursor.execute(""" 
		UPDATE sensorState 	
		SET state= %s 
		WHERE reference = %s
	""", (state1, reference1))
	
	cursor.execute(""" 
                UPDATE sensorState      
                SET state= %s 
                WHERE reference = %s
        """, (state2, reference2))
	

	dbConn.commit()

cursor.close()
