
import serial
import time

serial_port = '/dev/ttyACM0'
# 配置串口
ser = serial.Serial(
    port=serial_port,      # 串口号，根据你的设备修改，比如 '/dev/ttyUSB0'（Linux）
    baudrate=9600,    # 波特率
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1         # 超时设置（秒）
)

number_list = [11, 345, 66, 78]

# 发送字符串
for it in number_list:

    message = f"S={str(it)}\r\n"
    ser.write(message.encode('utf-8'))  # 发送 UTF-8 编码的字符串

    # 等待一会
    time.sleep(1)

# 关闭串口
ser.close()
