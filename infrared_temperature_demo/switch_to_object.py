## 转为测物体温度模式
import serial
import time

# 打开串口
ser = serial.Serial(
    port='/dev/ttyACM0',      # 或者 '/dev/ttyUSB0'，根据你的设备改
    baudrate=38400,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1                 # 秒为单位的超时时间
)

data_to_send = bytes.fromhex('AA A5 04 02 01 07 55') # 01 表示物温
ser.write(data_to_send)
print(f"已发送: {data_to_send.hex().upper()}")

time.sleep(0.3)  # 等待数据返回
if ser.in_waiting:
    received = ser.read(ser.in_waiting)
    ret = received.hex().upper()
    print(f"接收到: {ret}")

    if ret[8:10] == '00':
        print("设置测试物体温度模式成功 !!!")
# 关闭串口
ser.close()
