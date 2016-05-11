#import RPi.GPIO as GPIO
#import Controls
import Server

def serverTesting(): # only for testing .
	server = Server.qcServer(8080)
	
	server.startListening()
	print server.getPackets()
	#server.close()

serverTesting()


#GPIO.setmode(GPIO.BOARD)

#MotorFrontLeft = Cont.MotorControl(****port) #insert a port latter
#MotorFrontRight = Cont.MotorControl(****port) #insert a port latter
#MotorBackLeft = Cont.MotorControl(****port) #insert a port latter
#MotorBackRight = Cont.MotorControl(****port) #insert a port latter



#Finish
#GPIO.cleanup()

#TODO, make a client in Java Code .