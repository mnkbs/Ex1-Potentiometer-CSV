import serial
from datetime import datetime
import csv
from timeit import default_timer as timer
import argparse

parser = argparse.ArgumentParser(description='Serial communication')
parser.add_argument('port', type = int, help='USB port to use; 1 OR 2')
parser.add_argument('baudrate', type = int, help='Baudrate to use')
parser.add_argument('samples', type = int, help='Number of samples')

args = parser.parse_args()

if args.port == 1:
    _port = "/dev/cu.usbmodem141101"

elif args.port == 2:
    _port = "/dev/cu.usbmodem145101"


ser = serial.Serial(_port)
ser.flushInput()
ser.baudrate = args.baudrate
row = 1
count = 0

filename = datetime.now().strftime("%y-%m-%d_%H-%M-%S.csv")

with open(filename, "w") as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')
    writer.writerow(['S.No', 'Ellapsed', 'Time', 'Reading'])
    
    while True:
        ser_bytes = ser.readline()
        bytes_ = ser_bytes[0:len(ser_bytes)-2]
        decoded_bytes = bytes_.decode("ascii")
        print(decoded_bytes)

        time_now = datetime.now().strftime('%H-%M-%S-%f') [:-2]
        start = timer()
    
        writer.writerow([row, start, time_now, decoded_bytes])
        row += 1
        count += 1
        if  count > args.samples:
            break


