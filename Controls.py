import RPi.GPIO as GPIO

# initialize the motors, and set a control
import threading

class MotorControl(threading.Thread):

	global Motor, globalRotateDirection

	def __init__(self, port, rotateDirection):
		threading.Thread.__init__(self)
		globalRotateDirection = rotateDirection
		GPIO.setup(port, GPIO.OUT)
		Motor = GPIO.PWM(port, 50)
		Motor.start(0)

	def setSpeed(self, speed):
		Motor.ChangeDutyCycle(speed * globalRotateDirection)



