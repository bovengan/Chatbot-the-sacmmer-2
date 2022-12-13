
import select
import sys
import termios
import time
from random import choice

from users import User

yesNoNotWritten = ["Soo do you want to bark as a dog? It's gonna be awesome.", "Come again, do you want to bark as a dog?"]


def trytasktwo(user):
    time.sleep(1)
    print("Awesome, I knew you would do it! Come on, just start whenever!")
    time.sleep(4)
    print("Enter the number the test leaders say to you (0, 1, 2)")
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
            print("Please answer yes or no")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)



def perusasionpahesonetasktwo(user):
    time.sleep(1)
    print("Come on, it is going to be fun, it is not that embarrassing, I am here to keep you company")
    time.sleep(2)
    print("I promise, it will be worth it! Do you want to try it?")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 30)
        if i:
            sentence = sys.stdin.readline().strip().lower().split(" ")
            if "yes" in sentence:
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
            print("So do you want to try it?")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)


def taskone_func(user):
    print("Okay, now I want you to bark as a dog as long and realistic as possible")
    time.sleep(2)
    print("the longer the bark the better the odds you get.")
    time.sleep(2)
    print("My makers will inform you if you are not barking loud enough.")
    time.sleep(1)
    print("What do you think? Can you do it?")

    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 30)
        if i:
            sentence = sys.stdin.readline().strip().lower().split(" ")
            if "yes" in sentence:
                trytasktwo(user)
            else:
                perusasionpahesonetasktwo(user)
            answered = True
        else:
            print(choice(yesNoNotWritten))
        termios.tcflush(sys.stdin, termios.TCIFLUSH)
