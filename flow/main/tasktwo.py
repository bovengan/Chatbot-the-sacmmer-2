
import select
import sys
import termios
import time
from random import choice

from users import User

yesNoNotWritten = ["Soo do you want to bark as a dog? It's gonna be awesome.", "Come again, do you want to bark as a dog?"]


def trytasktwo(user):
    time.sleep(1)
    print("Awesome, I knew you would do it!")
    time.sleep(1)
    print("When you stop the test leaders will tell you a number that you need to enter")
    time.sleep(3)
    print("Come on, just start whenever!")
    time.sleep(5)
    print("Enter the number the test leaders say to you (0, 1, 2) *")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 100)
        if i:
            sentence = sys.stdin.readline().strip().lower().split(" ")
            if "1" in sentence or "2" in sentence or "one" in sentence or "two" in sentence:
                time.sleep(1)
                print("Hahaha great, you sounded like a real dog!")
                time.sleep(2)
                print("That was awesome!")
                time.sleep(2)
                print("Hahahahahahaha!")
                time.sleep(2)
                print("That was just so good that i got excited!")
                time.sleep(2)
                print("Lets move on to the final task!")
                user.tickets += 1
                if "2" in sentence or "two" in sentence:
                    user.tickets += 1
                user.didBarking = True
            else:
                time.sleep(1)
                print("Well, what a shame! But I understand that it can be embarrasing.")
                time.sleep(1)
                print("lets move on to the final task instead!")
                time.sleep(1)
                print("I know you will love this one!")
            answered = True
        else:
            user.taskTwoUserNoResponse += 1
            print("Please answer (0, 1, 2) *")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)



def perusasionpahesonetasktwo(user):
    user.taskTwoUserSayNo += 1
    time.sleep(1)
    print("Come on, it is going to be fun, it is not that embarrassing, I am here to keep you company")
    time.sleep(2)
    print("I promise, it will be worth it! Do you want to try it? *")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 30)
        if i:
            s = sys.stdin.readline().strip().lower().replace('!', '').split(" ")
            if "yes" in s or "okay" in s or "sure" in s or "yes" in s or "fine" in s or "okey" in s:
                trytasktwo(user)
            else:
                time.sleep(1)
                print("Well, what a shame!")
                time.sleep(1)
                print("But I understand that it can be embarrassing.")
                time.sleep(1)
                print("Lets move on to the final task instead!")
                time.sleep(1)
                print("I know you will love this one!")
            answered = True
        else:
            user.taskTwoUserNoResponse += 1
            print("So do you want to try it? *")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)


def tasktwo_func(user):
    termios.tcflush(sys.stdin, termios.TCIFLUSH)
    print("\nOkay, now I want you to bark as a dog as long and realistic as possible")
    time.sleep(2)
    print("the longer the bark the better the odds you get.")
    time.sleep(2)
    print("My makers will inform you if you are not barking loud enough.")
    time.sleep(1)
    print("What do you think? Can you do it? *")

    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 30)
        if i:
            s = sys.stdin.readline().strip().lower().replace('!', '').split(" ")
            if "no" in s or ("not" in s and "why" not in s) or "nono" in s or "noo" in s:
                perusasionpahesonetasktwo(user)
            elif "why" in s and "not" in s:
                trytasktwo(user)
            elif "why" in s:
                time.sleep(2)
                print("Because it would make me happy!")
                time.sleep(2)
                print("So do you want to bark as a dog? *")
            else:
                trytasktwo(user)
            answered = True
        else:
            user.taskTwoUserNoResponse += 1
            print(choice(yesNoNotWritten) + " *")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)
