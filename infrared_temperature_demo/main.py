import serial
import time

def split_hex_string(hex_str):
    # 每两个字符分割一次
    return [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]

def parse_temperature(hex_str):
    # 输入为 "0129" 这样的 16 进制字符串
    # 去掉可能的前缀，保证是4位字符串
    hex_str = hex_str.zfill(4)
    
    # 拆分成高低字节
    high_byte = int(hex_str[:2], 16)
    low_byte = int(hex_str[2:], 16)

    # 计算温度
    temperature = (low_byte + high_byte * 256) / 10
    return temperature

# 打开串口
ser = serial.Serial(
    port='/dev/ttyACM0',      # 或者 '/dev/ttyUSB0'，根据你的设备改
    baudrate=38400,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1                 # 秒为单位的超时时间
)

## 发送格式
# AA A5 包长度 测温命令 参数内容(可以为空) 全加校验(包长+命令+参数) 55
send_to_get = 'AA A5 03 01 04 55' # 参数内容为空


while True:
    data_to_send = bytes.fromhex(send_to_get) # 发送 16 进制数据
    ser.write(data_to_send)
    print(f"已发送: {data_to_send.hex().upper()}")

    # 接收数据格式
    # AA A5 08 命令字节 测温类型(1为物温、2为体温) 目标温度高位 目标温度低位 环境温度高位 环境温度低位 全加校验 55
    time.sleep(0.3)  # 等待数据返回
    if ser.in_waiting:
        received = ser.read(ser.in_waiting)     # 读取串口数据
        hex_data = received.hex().upper()       # 转为 16 进制字符串
        hex_list = split_hex_string(hex_data)   # 按每两位分割字符串
        print(f"接收到: {hex_list}")

        # 开始解析
        temperature_type = hex_list[4] # 测温类型(1为物温、2为体温)
        if temperature_type == '01':
            temperature_type = '被测物体温度为: '
        else:
            temperature_type = '当前体温为: '

        target_temperature = parse_temperature(hex_list[5] + hex_list[6]) # 被测物体或者人体温度

        environment_temperature = parse_temperature(hex_list[7] + hex_list[8]) # 环境温度

        print(f"{temperature_type}{target_temperature}, 环境温度：{environment_temperature}")

    else:
        print("未接收到数据")

# 关闭串口
ser.close()
