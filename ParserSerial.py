import sys
from datetime import datetime
import time
import csv
import argparse
import serial
import struct

parser = argparse.ArgumentParser(description='Potentiometer Readings')
parser.add_argument('port', type = int, help='USB port to use; 1 OR 2')
parser.add_argument('baudrate', type = int, help='Baudrate to use')
#parser.add_argument('no_samples', type = int, help='Number of samples')
parser.add_argument('record_secs', type = int, help='Seconds to record')
parser.add_argument('print_data', type = str, help='Print - y/n')
args = parser.parse_args()

if args.port == 1:
    port_ = "/dev/cu.usbmodem141101"

elif args.port == 2:
    port_ = "/dev/cu.usbmodem145101"

ser = serial.Serial(port_)
ser.flushInput()
ser.baudrate = args.baudrate
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE

row = 1
#count = 0

filename = datetime.now().strftime("%y-%m-%d_%H-%M-%S.csv")
with open(filename, "w") as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')
    writer.writerow(['S.No', 'Ellapsed', 'Reading'])
    start_time = time.time()

    while True:
        start_byte = ser.read(size = 1)
        start = int.from_bytes(start_byte, byteorder=sys.byteorder)
        if start == 0x3A:

            lsb_bytes = ser.read(size = 1) 
            lsb = int.from_bytes(lsb_bytes, byteorder=sys.byteorder)
            msb_bytes = ser.read (size = 1)
            msb = int.from_bytes(msb_bytes, byteorder=sys.byteorder)
            val = (lsb << 8) + msb; 

            time_bytes = ser.read(size = 4) 
            time_ = struct.unpack('i', time_bytes)[0]
            stime = time_/1000

            if args.print_data == 'y':
                print(val)
                print(stime)

            writer.writerow([row, stime , val])
            row += 1
            #count += 1
            # #if  count > args.no_samples:
            #  break
            if stime > args.record_secs:
                break
