#import RPi.GPIO as GPIO
#import Controls
import Server


def serverTesting(): # only for testing .

	#configuration
	ServerHandler = Server.qcServer(8080)
	serverThread = Server.openServerThread(ServerHandler)
	serverThread.start()
	try:
		while True:
			Hello = 1
	except Exception:
		ServerHandler.closeServer()
		return 0

serverTesting()


#GPIO.setmode(GPIO.BOARD)

#MotorFrontLeft = Controls.MotorControl(****port, 1) #insert a port latter and the kivun sivuv
#MotorFrontRight = Controls.MotorControl(****port, -1) #insert a port latter and the kivun sivuv
#MotorBackLeft = Conttrols.MotorControl(****port, -1) #insert a port latter and the kivun sivuv
#MotorBackRight = Controls.MotorControl(****port, 1) #insert a port latter and the kivun sivuv
#MotorFrontLeft.start()
#MotorFrontRight.start()
#MotorBackLeft.start()
#MotorBackRight.start()

#Finish

#GPIO.cleanup()

#TODO, make a client in Java Code .