#!/usr/bin/env python

import wiringpi as GPIO
from time import sleep
LED_PIN = 24
GPIO.wiringPiSetupGpio()

GPIO.pinMode (LED_PIN,GPIO.OUTPUT)
GPIO.digitalWrite (LED_PIN,GPIO.HIGH)
sleep(2)
GPIO.digitalWrite (LED_PIN,GPIO.LOW)


