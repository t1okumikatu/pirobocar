import wiringpi as wp

class CarController(object):

    FORWARD_PIN = 22
    BACKWARD_PIN = 22

    STEER_PIN = 18
    STEER_MIN = 65
    STEER_MAX = 89

    def __init__(self):
        # slottle
        wp.wiringPiSetupGpio()
        wp.pinMode(CarController.FORWARD_PIN,1)
        wp.softPwmCreate(CarController.FORWARD_PIN,0,100)
        wp.pinMode(CarController.BACKWARD_PIN,1)
        wp.softPwmCreate(CarController.BACKWARD_PIN,0,100)
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
            wp.softPwmWrite(CarController.FORWARD_PIN,abs(x))
            wp.softPwmWrite(CarController.BACKWARD_PIN,0)
        if x<0:
            wp.softPwmWrite(CarController.FORWARD_PIN,0)
            wp.softPwmWrite(CarController.BACKWARD_PIN,abs(x))

    def steer(self,x):
        """
        x: -1.0 to 1.0
        """
        a = 0.5 * (CarController.STEER_MAX - CarController.STEER_MIN)
        b = 0.5 * (CarController.STEER_MAX + CarController.STEER_MIN)
        x = int(max(CarController.STEER_MIN,min(CarController.STEER_MAX, a*x+b)))
        wp.pwmWrite(CarController.STEER_PIN,x)

    def brake(self):
        wp.softPwmWrite(CarController.FORWARD_PIN,100)
        wp.softPwmWrite(CarController.BACKWARD_PIN,100)

