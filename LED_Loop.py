import RPi.GPIO as GPIO
import time


def switch_callback(gpio_pin):
    print(gpio_pin)
    GPIO.output(15,GPIO.HIGH)


GPIO.setmode(GPIO.BCM)  #GPIOへアクセスする番号をBCMの番号で指定することを宣言します。                        
GPIO.setup(15,GPIO.OUT) #BCMの15番ピン、物理的には10番ピンを出力に設定します。                                
GPIO.setup(2,GPIO.IN)   #BCM 2番ピンを入力に設定します。                                                      

GPIO.add_event_detect(2, GPIO.FALLING,bouncetime=100)
GPIO.add_event_callback(2, switch_callback) #スイッチ入力端子の状態ををcallbackのトリガとして指定します。     

try:
    while True:
        GPIO.output(15,GPIO.LOW)
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()

