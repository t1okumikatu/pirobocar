import wiringpi as wp

class CarController(object):

    DIRECTION_PIN = 22
    PWM_PIN = 23

    STEER_PIN = 18
    STEER_MIN = 65
    STEER_MAX = 89

    def __init__(self):
        # slottle
        wp.wiringPiSetupGpio()
        wp.pinMode(CarController.DIRECTION_PIN,pinout)
        wp.softPwmCreate(CarController.PWM_PIN,0,100)
        wp.pinMode(CarController.DIRECTION_PIN,pinout)
        wp.softPwmCreate(CarController.PWM_PIN,0,100)
        # steering
        wp.wiringPiSetupGpio()
        wp.pinMode(CarController.STEER_PIN,2) # Hardware PWM
        wp.pwmSetMode(0)
        wp.pwmSetRange(1024)
        wp.pwmSetClock(375)
 
    def slottle(self,x):
        """
        x: -1.0 to 1.0
        """
        x = int(max(-100,min(100,100*x)))
        if 0<=x:
            wp.softPwmWrite(CarController.PWM_PIN,abs(x))
            wp.softPwmWrite(CarController.DIRECTION_PIN,0)
        if x<0:
            wp.softPwmWrite(CarController.PWM_PIN,abs(x))
            wp.softPwmWrite(CarController.DIRECTION_PIN,1)

    def steer(self,x):
        """
        x: -1.0 to 1.0
        """
        a = 0.5 * (CarController.STEER_MAX - CarController.STEER_MIN)
        b = 0.5 * (CarController.STEER_MAX + CarController.STEER_MIN)
        x = int(max(CarController.STEER_MIN,min(CarController.STEER_MAX, a*x+b)))
        wp.pwmWrite(CarController.STEER_PIN,x)

    def brake(self):
        wp.softPwmWrite(CarController.PWM_PIN,0)
 

