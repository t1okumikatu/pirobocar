import wiringpi as pi
import time
LED_PIN=24
pi.wiringPiSetupGpio()
pi.pinMode(LED_PIN, pi.OUTPUT)
pi.softPwmCreate(LED_PIN, 0,100)
for j in range(0,11):
    for i in range(1,100):
        pi.softPwmWrite(LED_PIN, i)
        time.sleep(0.1)

    for i in reversed(range(1,100)):
        pi.softPwmWrite(LED_PIN, i)
        time.sleep(0.1)

pi.digitalWrite(LED_PIN, pi.LOW)
