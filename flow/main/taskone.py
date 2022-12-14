
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
    print("Answer yes or no if the task leaders informed you that you completed the task or not *")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 15)
        if i:
            s = sys.stdin.readline().strip().lower().replace('!', '').split(" ")
            if "yes" in s or "okay" in s or "sure" in s or "yes" in s or "fine" in s or "okey" in s:
                time.sleep(1)
                print("Good job! You looked like a real athlete doing that. Let's move onto the second task.")
                user.tickets += 1
                user.ranAroundTable = True
            else:
                time.sleep(1)
                print("Well, what a shame!")
                time.sleep(1)
                print("But I understand that it can be embarrassing.")
                time.sleep(2)
                print("Lets move on to the final task instead!")
                time.sleep(2)
                print("I know you will love this one!")
            answered = True
        else:
            user.taskOneUserNoResponse += 1
            print("Please answer yes or no *")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)


def perusasionpahesonetaskone(user):
    user.taskOneUserSayNo += 1
    time.sleep(1)
    print("I promise, it will be worth it! Do you want to try it? *")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 15)
        if i:
            s = sys.stdin.readline().strip().lower().replace('!', '').split(" ")
            if "no" in s or ("not" in s and "why" not in s) or "nono" in s or "noo" in s:
                perusasionpahestwotaskone(user)
            else:
                trytask(user)
            answered = True
        else:
            user.taskOneUserNoResponse += 1
            print("So do you want to try it? *")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)


def perusasionpahestwotaskone(user):
    user.taskOneUserSayNo += 1
    time.sleep(1)
    print("Come on, you are only " + str(user.age) + " years old, no one expects you to be mature.")
    time.sleep(2)
    print("Last time I will ask, do you want to run around the table? *")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 15)
        if i:
            s = sys.stdin.readline().strip().lower().replace('!', '').split(" ")
            if "no" in s or ("not" in s and "why" not in s) or "nono" in s or "noo" in s:
                print("Well, what a shame!")
                time.sleep(2)
                print("But I understand that it can be embarrassing")
                time.sleep(3)
                print("lets move on to the final task instead!")
                time.sleep(2)
                print("I know you will love this one!")
            else:
                trytask(user)
            answered = True
        else:
            user.taskOneUserNoResponse += 1
            print("So do you want to try it? *")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)


def taskone_func(user):
    termios.tcflush(sys.stdin, termios.TCIFLUSH)
    print("\nOkay great, here is the first task.")
    time.sleep(2)
    print("I want you to run around this table as fast as you can.")
    time.sleep(2)
    print("What do you think? Can you do it? *")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 30)
        if i:
            s = sys.stdin.readline().strip().lower().replace('!', '').split(" ")
            if "no" in s or ("not" in s and "why" not in s) or "nono" in s or "noo" in s:
                perusasionpahesonetaskone(user)
            elif "why" in s and "not" in s:
                trytask(user)
            elif "why" in s:
                time.sleep(2)
                print("Because it would make me happy!")
                time.sleep(2)
                print("So do you want to run around the table? *")
            else:
                trytask(user)
            answered = True
        else:
            user.taskOneUserNoResponse += 1
            print(choice(yesNoNotWritten) + " *")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)

#taskone_func(User(12234, 45, 45))
