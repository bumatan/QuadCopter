from Devices import motor

def run_motor_test(test_value):
    """
    docstring
    """
    motor1 = motor.Motor(17)
    motor2 = motor.Motor(18)
    motor3 = motor.Motor(19)
    motor4 = motor.Motor(20)

    motor1.setValue(test_value)
    motor2.setValue(test_value)
    motor3.setValue(test_value)
    motor4.setValue(test_value)

    motor1.applyMotorValue()
    motor2.applyMotorValue()
    motor3.applyMotorValue()
    motor4.applyMotorValue()

    assert motor1.getMotorValue() == test_value
    assert motor2.getMotorValue() == test_value
    assert motor3.getMotorValue() == test_value
    assert motor4.getMotorValue() == test_value   