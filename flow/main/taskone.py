
import select
import sys
import termios
import time
from random import choice

from users import User

yesNoNotWritten = ["Can you do it?", "Come on, can you do it?", "Please type yes or no"]


def trytask(user):
    time.sleep(1)
    print("Awesome, I knew you would do it! Come on, just start whenever!")
    time.sleep(4)
    print("Answer yes or no if the task leaders informed you that you completed the task or not")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 15)
        if i:
            sentence = sys.stdin.readline().strip().lower().split(" ")
            if "yes" in sentence:
                print("Good job! You looked like a real athlete doing that. Let's move onto the second task.")
            else:
                print(
                    "Well, what a shame! But I understand that it can be embarrassing, lets move on to the final task instead!")
                print("I know you will love this one!")
            answered = True
        else:
            print("Please answer yes or no")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)


def perusasionpahesonetaskone(user):
    time.sleep(1)
    print("I promise, it will be worth it! Do you want to try it?")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 15)
        if i:
            sentence = sys.stdin.readline().strip().lower().split(" ")
            if "yes" in sentence:
                trytask(user)
            else:
                perusasionpahestwotaskone(user)
            answered = True
        else:
            print("So do you want to try it?")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)


def perusasionpahestwotaskone(user):
    time.sleep(1)
    print("Come on, you are only " + str(user.age) + " years old, no one expects you to be mature.")
    time.sleep(2)
    print("Last time I will ask, do you want to run around the table?")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 15)
        if i:
            sentence = sys.stdin.readline().strip().lower().split(" ")
            if "yes" in sentence or "okay" in sentence:
                trytask(user)
            else:
                print("Well, what a shame!")
                time.sleep(1)
                print("But I understand that it can be embarrassing")
                time.sleep(2)
                print("lets move on to the final task instead!")
                time.sleep(1)
                print("I know you will love this one!")
            answered = True
        else:
            print("So do you want to try it?")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)


def taskone_func(user):
    print("Okay great, here is the first task.")
    time.sleep(2)
    print("I want you to run around this table as fast as you can.")
    time.sleep(2)
    print("What do you think? Can you do it?")

    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 5)
        if i:
            sentence = sys.stdin.readline().strip().lower().split(" ")
            if "yes" in sentence:
                trytask(user)
            else:
                perusasionpahesonetaskone(user)
            answered = True
        else:
            print(choice(yesNoNotWritten))
        termios.tcflush(sys.stdin, termios.TCIFLUSH)

#taskone_func(User(12234, 45, 45))
