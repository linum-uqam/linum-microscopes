import pyfirmata2
import time

# https://realpython.com/arduino-python/

board = pyfirmata2.Arduino("COM14")

while True:
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)