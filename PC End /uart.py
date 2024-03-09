import serial
import time

ser = serial.Serial('COM3', 2400)

start_time = time.time()

while True:
    if ser.in_waiting > 0:
        start_time = time.time()
        line = ser.readline().decode('utf-8').rstrip()
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        size_in_bits = len(line)   
        speed = size_in_bits / elapsed_time

        #print(f"Data: {line}")
        print(f"speed: {speed} bits/second")
        time.sleep(1)