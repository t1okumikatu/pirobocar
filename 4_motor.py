#!/usr/bin/env python
#-*-coding: UTF-8-*-
# GPIOを制御するライブラリ
import wiringpi
# タイマーのライブラリ
import time
# 引数取得
import sys

# GPIO端子の設定
Amotor1_pin = 22
Amotor2_pin = 23
Bmotor1_pin = 17
Bmotor2_pin = 27
# 引数
param = sys.argv

# 第1引数
# go : 回転
# back : 逆回転
# break : ブレーキ
order = param[1]

# 第2引数 秒数
second = int(param[2])

# GPIO出力モードを1に設定する
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(Amotor1_pin, 1 )
wiringpi.pinMode(Amotor2_pin, 1 )
wiringpi.pinMode(Bmotor1_pin, 1 )
wiringpi.pinMode(Bmotor2_pin, 1 )
if order == "go":
    if second == 0:
        print("回転 止めるときはbreak 0コマンド！")
    else:
        print(str(second)+"秒回転")
    wiringpi.digitalWrite(Amotor1_pin, 1 )
    wiringpi.digitalWrite(Amotor2_pin, 1 )
    wiringpi.digitalWrite(Bmotor1_pin, 1 )
    wiringpi.digitalWrite(Bmotor2_pin, 1 )
    time.sleep(second)
elif order == "back":
    if second == 0:
        print("逆回転 止めるときはbreak 0コマンド！")
    else:
        print(str(second)+"秒逆回転")
    wiringpi.digitalWrite(Amotor1_pin, 0 ) 
    wiringpi.digitalWrite(Amotor2_pin, 1 )
    wiringpi.digitalWrite(Bmotor1_pin, 0 )
    wiringpi.digitalWrite(Bmotor2_pin, 1 )
    time.sleep(second)

# 第2引数が0の場合は、ブレーキをしない
# 第1引数がbreakの場合は、ブレーキ
if order == "break" or second != 0:
    print("ブレーキ！")
    wiringpi.digitalWrite(Amotor1_pin, 1 )
    wiringpi.digitalWrite(Amotor2_pin, 0 )
    wiringpi.digitalWrite(Bmotor1_pin, 1 )
    wiringpi.digitalWrite(Bmotor2_pin, 0 )

