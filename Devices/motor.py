#from RPi.GPIO import GPIO #TODO delete this when you add a test file

class Motor(object):
    """
    Object for all the commands you want to do on a motor.
    """
    def __init__(self, channel, rotationDirection="clockwise"):
        """
        Inits the motor configuration.
        """
        self.rotationDirection = rotationDirection
        self.motorValue = 0.0
        self.channel = channel
        self.frequency = 0.5 # TODO test some frequencey configurations
        
        # Set the GPIO Module
        #GPIO.setmode(GPIO.BOARD)
        #GPIO.setup(self.channel, GPIO.OUT)
        #self.motorPWM = GPIO.PWM(self.channel, self.frequency)
        #self.motorPWM.start(self.motorValue)

    def setValue(self, value):
        """
        Sets the motor value.
        Motor value should be between 0 to 100
        """

        # Normalize motor value
        if value > 100: #TODO change the magic number to a package parameter
            value = 100.0
        elif value < 0: #TODO change the magic number to a package parameter
            value = 0.0

        # Sets the mottor value
        self.motorValue = value

        # Update the motor frequencey
        self.applyMotorValue()
        
    def addToMotorValue(self, valueToAdd):
        """
        Function allows you to only add a value to a motor.
        """
        self.setValue(self.motorValue + valueToAdd)

    def applyMotorValue(self):
        """
        Apply the value set to the motor
        """
        #self.motorPWM.ChangeDutyCycle(self.motorValue)

    def getMotorValue(self):
        """
        docstring
        """
        return self.motorValue