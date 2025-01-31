import pyfirmata2
import time

# https://realpython.com/arduino-python/

board = pyfirmata2.Arduino("COM6")

while True:
    board.digital[2].write(1)
    time.sleep(1)
    board.digital[2].write(0)
    time.sleep(1)