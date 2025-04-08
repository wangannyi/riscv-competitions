#coding: UTF-8
import sys
import time
sys.path.append("..")  # Append the parent directory to the system path for module imports
from lib import TOF_Sense  # Import the TOF_Sense module from the 'lib' directory

tof = TOF_Sense.TOF_Sense('/dev/ttyACM0', 921600)

# Main loop to continuously perform TOF (Time-of-Flight) decoding
try:
    while True:  # Infinite loop to keep the program running
        # 打印信息
        tof.TOF_Active_Decoding()  # Perform active TOF decoding (Active Output Example)
        # tof.TOF_Inquire_Decoding(0)  # Uncomment this line to perform query-based TOF decoding (Example query output)
        time.sleep(0.02)  # Sleep for 0.02 seconds (default refresh rate is 50Hz; for 100Hz, use 0.01 seconds)

except KeyboardInterrupt:  # Handle the KeyboardInterrupt exception to allow graceful exit
    print("Quit.")  # Print a message indicating the program is quitting