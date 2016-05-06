import RPi.GPIO as GPIO

# initialize the motors, and set a control

class MotorControl:

	global Motor

	def __init__(self, port):
		GPIO.setup(port, GPIO.OUT)
		Motor = GPIO.PWM(port, 50)
		Motor.start(0)

	def setSpeed(self, speed):
		Motor.ChangeDutyCycle(-speed)



