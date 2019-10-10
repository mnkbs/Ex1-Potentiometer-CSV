import serial

ser = serial.Serial('/dev/cu.usbmodem145101')
ser.flushInput()

i = 0

while True:
    ser_bytes = ser.readline()
    bytes_ = ser_bytes[0:len(ser_bytes)-2]
    decoded_bytes = bytes_.decode("utf-8")
    print(decoded_bytes)

    i += 1
    if i > 10:
        break

