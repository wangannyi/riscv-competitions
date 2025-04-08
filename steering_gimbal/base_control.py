# 使用 lgpio 作为引脚底层
from gpiozero.pins.lgpio import LGPIOFactory
from gpiozero import Device
Device.pin_factory = LGPIOFactory(chip=0)

# 伺服电机类
from gpiozero import Servo
from time import sleep

pin_number = 73

servo = Servo(pin_number)

# 范围从 -1（最小位置）到 1（最大位置）

while True:
    user_input = input("请输入一个在 -1 到 1 之间的浮点数：")
    try:
        value = float(user_input)
        if -1 <= value <= 1:
            servo.value = value
        else:
            print("输入的数字不在范围内，请重新输入。")
    except ValueError:
        print("无效输入，请输入一个浮点数。")