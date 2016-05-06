import RPi.GPIO as GPIO
import Controls

GPIO.setmode(GPIO.BOARD)

MotorFrontLeft = Cont.MotorControl(****port) #insert a port latter
MotorFrontRight = Cont.MotorControl(****port) #insert a port latter
MotorBackLeft = Cont.MotorControl(****port) #insert a port latter
MotorBackRight = Cont.MotorControl(****port) #insert a port latter



#Finish
GPIO.cleanup()