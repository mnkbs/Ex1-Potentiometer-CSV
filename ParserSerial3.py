import serial
from datetime import datetime
import time
import csv
import argparse

parser = argparse.ArgumentParser(description='Serial communication')
parser.add_argument(('port', type = int, help='USB port to use; 1 OR 2'),
                    ('baudrate', type = int, help='Baudrate to use'),
                    #('samples', type = int, help='Number of samples'),
                    ('secs', type = int, help='Seconds to record'),
                    ('printing', type = str, help='Print - y/n'))

args = parser.parse_args()

if args.port == 1:
    _port = "/dev/cu.usbmodem141101"

elif args.port == 2:
    _port = "/dev/cu.usbmodem145101"

ser = serial.Serial(_port,
                    baudrate = args.baudrate
                    bytesize = serial.EIGHTBITS
                    parity = serial.PARITY_NONE
                    stopbits = serial.STOPBITS_ONE
                    timeout = None)
ser.flushInput()

row = 1
#count = 0

filename = datetime.now().strftime("%y-%m-%d_%H-%M-%S.csv")

with open(filename, "w") as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')
    writer.writerow(['S.No', 'Ellapsed', 'Time', 'Reading'])
    start_time = time.time()

    while True:
        #ser.reset_input_buffer()
        ser_bytes = ser.read()
        #bytes_ = ser_bytes[0:len(ser_bytes)]
        decoded_bytes = ser_bytes.decode("utf-8")
        if args.printing == 'y':
            print(decoded_bytes)

        time_now = datetime.now().strftime('%H-%M-%S-%f') [:-2]
        elapsed_time = time.time() - start_time
    
        writer.writerow([row, elapsed_time, time_now, decoded_bytes])
        row += 1
        #count += 1

        #if  count > args.samples:
          #  break
        if elapsed_time > args.secs:
            break
