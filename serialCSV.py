
import serial
from datetime import datetime
import csv
from timeit import default_timer as timer

ser = serial.Serial('/dev/cu.usbmodem145101')
ser.flushInput()
ser.baudrate = 115200

row = 1
number = 0

filename = datetime.now().strftime("%y-%m-%d_%H-%M-%S.csv")

with open(filename, "w") as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')
    writer.writerow(['S.No', 'Ellapsed', 'Time', 'Reading'])
    
    while True:
        ser_bytes = ser.readline()
        bytes_ = ser_bytes[0:len(ser_bytes)-2]
        decoded_bytes = bytes_.decode("utf-8")
        print(decoded_bytes)

        time_now = datetime.now().strftime('%H-%M-%S-%f') [:-2]
        start = timer()
    
        writer.writerow([row, start, time_now, decoded_bytes])
        row += 1
        number += 1
        if  number > 600:
            break


