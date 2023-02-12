import serial
import time
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


while True:
    feedback_data = write_read("1")
    print(feedback_data.decode())
    time.sleep(1.0)
    feedback_data = write_read(")")
    print(feedback_data.decode())
    time.sleep(1.0)
