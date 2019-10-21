#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import wiringpi as pi
import time

POWER_SW_PIN = 4


IN1_MOTOR_PIN = 22
IN2_MOTOR_PIN = 23

pi.wiringPiSetupGpio()
pi.pinMode( POWER_SW_PIN, pi.INPUT )
pi.pinMode( IN1_MOTOR_PIN, pi.OUTPUT )
pi.pinMode( IN2_MOTOR_PIN, pi.OUTPUT )
pi.pullUpDnControl( POWER_SW_PIN, pi.PUD_DOWN )


pi.softPwmCreate( IN1_MOTOR_PIN, 0, 1 )
pi.softPwmCreate( IN2_MOTOR_PIN, 0, 100 )


pi.softPwmWrite( IN1_MOTOR_PIN, 0 )
pi.softPwmWrite( IN2_MOTOR_PIN, 0 )


countPower = 0


try:
    while True:

        if ( pi.digitalRead( POWER_SW_PIN ) == pi.HIGH ):
            time.sleep( 0.5 )


            countPower = countPower + 1


            if countPower % 5 == 1:
                pi.softPwmWrite( IN1_MOTOR_PIN, 1 )
                pi.softPwmWrite( IN2_MOTOR_PIN, 25 )
                print("微風")
            elif countPower % 5 == 2:
                pi.softPwmWrite( IN1_MOTOR_PIN, 0 )
                pi.softPwmWrite( IN2_MOTOR_PIN, 50 )
                print("弱風")
            elif countPower % 5 == 3:
                pi.softPwmWrite( IN1_MOTOR_PIN, 0 )
                pi.softPwmWrite( IN2_MOTOR_PIN, 75 )
                print("強風")
            elif countPower % 5 == 4:
                pi.softPwmWrite( IN1_MOTOR_PIN, 0 )
                pi.softPwmWrite( IN2_MOTOR_PIN, 100 )
                print("最大")
            else:
                pi.softPwmWrite( IN1_MOTOR_PIN, 0 )
                pi.softPwmWrite( IN2_MOTOR_PIN, 0 )
                print("停止\n")


            while ( pi.digitalRead( POWER_SW_PIN ) == pi.LOW ):
                time.sleep( 0.1 )

            time.sleep( 0.1 )


except KeyboardInterrupt:
    pi.softPwmWrite( IN1_MOTOR_PIN, 0 )
    pi.softPwmWrite( IN2_MOTOR_PIN, 0 )
    print("Stop")

