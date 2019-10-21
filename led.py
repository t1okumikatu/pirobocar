 #!/usr/bin/python3
 # -*- coding: utf-8 -*-

 import time
 import pigpio #pigpioライブラリをインポートする

 pi = pigpio.pi() #GPIOにアクセスするためのインスタンスを作成します
 pi.set_mode(24, pigpio.OUTPUT) #GPIOのモードを設定します他にINPUTとかある。18はGPIO18の18番です。

 while True:
       pi.write(24, 1) #GPIO18番のレベルをHIGHにします
       time.sleep(0.5)
       pi.write(24, 0) #GPIO18番のレベルをLOWにします
       time.sleep(0.5)

