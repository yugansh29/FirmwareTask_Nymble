import serial
import time

# Open the serial port. Replace 'COM3' with the correct port for your system.
ser = serial.Serial('COM3', 2400)

start_time = time.time()

while True:
    if ser.in_waiting > 0:
        start_time = time.time()
        line = ser.readline().decode('utf-8').rstrip()
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        size_in_bits = len(line) * 8  # each character is 1 byte = 8 bits
        speed = size_in_bits / elapsed_time if elapsed_time > 0 else 0

        #print(f"Data: {line}")
        print(f"Transmission speed: {speed} bits/second")
        time.sleep(1)