import select
import sys
import termios
from random import choice
from time import sleep

greetings = ["Hi there", "Hello there"]
while True:
    print(choice(greetings) + ' *')

    i, o, e = select.select([sys.stdin], [], [], 10)

    if i:
        pass
    else:
        pass
    termios.tcflush(sys.stdin, termios.TCIFLUSH)
    print("Try again")