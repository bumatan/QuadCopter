#import RPi.GPIO as GPIO
#import Controls
import Server
import CommandParser
import CommandMaker

def serverTesting(): # only for testing .
	
	#configuration
	Server = Server.qcServer(8080)
	Server.startListening() #Start Listening
	
	#doCommands
	Commands = CommandParser.getCommand(Server)
	CommandMaker.controlCommands(Commands)




	server.close()

serverTesting()


#GPIO.setmode(GPIO.BOARD)

#MotorFrontLeft = Cont.MotorControl(****port) #insert a port latter
#MotorFrontRight = Cont.MotorControl(****port) #insert a port latter
#MotorBackLeft = Cont.MotorControl(****port) #insert a port latter
#MotorBackRight = Cont.MotorControl(****port) #insert a port latter



#Finish
#GPIO.cleanup()

#TODO, make a client in Java Code .