#import RPi.GPIO as GPIO
#import Controls
import Server
import CommandParser
import CommandMaker

def serverTesting(): # only for testing .
	
<<<<<<< HEAD
	#configuration
	Server = Server.qcServer(8080)
	Server.startListening() #Start Listening
	
	#doCommands
	Commands = CommandParser.getCommand(Server)
	CommandMaker.controlCommands(Commands)




	server.close()
=======
	server.startListening()
	print server.getPackets()
	#server.close()
>>>>>>> c7f0dc913494cdc159e72dbc3192ab4173d5446d

serverTesting()


#GPIO.setmode(GPIO.BOARD)

#MotorFrontLeft = Cont.MotorControl(****port) #insert a port latter
#MotorFrontRight = Cont.MotorControl(****port) #insert a port latter
#MotorBackLeft = Cont.MotorControl(****port) #insert a port latter
#MotorBackRight = Cont.MotorControl(****port) #insert a port latter



#Finish
#GPIO.cleanup()

#TODO, make a client in Java Code .