import sys
from os import path

if __name__ == '__main__':
    sys.path.append( path.dirname( path.abspath(__file__) ) ) # TODO Very ugly, need to see how we can change it

    from tests import motor_test
    motor_test.run_motor_test(100)
    print ("Hey")


