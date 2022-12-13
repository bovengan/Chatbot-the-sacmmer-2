import select
import sys
import termios
import time
from random import choice

from users import User

yesNoNotWritten = ["I didn't quite hear you. Soo do you want scare the people working out there?",
                   "Do you want to pretend to be a T-rex?",
                   "One more time. Do you want to be a T-rex?"]


def trytaskthree(user):
    time.sleep(1)
    print("Marvelous, I knew you would do it! Don't scare me to much now though!")
    time.sleep(2)
    print("But just go out and start whenever you are ready!")
    time.sleep(4)
    print("Answer yes or no if the task leaders informed you that you completed the task or not")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 200)
        if i:
            sentence = sys.stdin.readline().strip().lower().split(" ")
            if "yes" in sentence:
                user.tickets += 1
                time.sleep(1)
                print("HELP, do not come closer! I am convinced you are a T-rex now!")
                time.sleep(3)
                print("Oh sorry, i lost it again! But well done i guess! Lets move on to the final task!")
            else:
                time.sleep(1)
                print("Well, well, well, well. Valid effort but not nearly good enough!")
                time.sleep(2)
                print("That's an F for this task, but let's move on to the final!")
            answered = True
        else:
            user.taskThreeUserNoResponse += 1
            print("Please answer yes or no")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)


def perusasionpahesonetaskthree(user):
    time.sleep(1)
    print("Really? I think T-REXes are soo cool! I would love it of you did it!")
    time.sleep(2)
    print("This can be epic! Think about it!")
    time.sleep(1)
    if user.didBarking & user.ranAroundTable:
        print("You already barked, and ran around this table...")
        time.sleep(2)
        print("This is not any worse than that, right?")
    elif user.didBarking:
        print("You already barked like a mad dog!")
        time.sleep(2)
        print("The damage is already done, this is not worse, right?")
    elif user.ranAroundTable:
        print("You have already been up and running!")
        time.sleep(2)
        print("Think of this as an extension of that!")
    time.sleep(2)
    print("So do you want to do the T-rex?")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 30)
        if i:
            s = sys.stdin.readline().strip().lower().replace('!', '').split(" ")
            if "yes" in s or "okay" in s or "sure" in s or "yes" in s or "fine" in s or "okey" in s:
                trytaskthree(user)
            else:
                print("Okay, okay! You are a scared i guess!")
                time.sleep(2)
                print("Lets move on to the final task instead!")
            answered = True
        else:
            user.taskThreeUserNoResponse += 1
            print("So do you want to try it?")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)


def taskthree_func(user):
    print("Okay, so wouldn't it be fun if you now go out in the corridor and pretend that you are the dinosaur T-REX?")
    time.sleep(3)
    print("And you should both look like one and sound like a T-REX! That would be awesome!")
    time.sleep(2)
    print("So is this something for you?")

    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 30)
        if i:
            s = sys.stdin.readline().strip().lower().replace('!', '').split(" ")
            if "yes" in s or "okay" in s or "sure" in s or "yes" in s or "fine" in s or "okey" in s:
                trytaskthree(user)
            else:
                perusasionpahesonetaskthree(user)
            answered = True
        else:
            user.taskThreeUserNoResponse += 1
            print(choice(yesNoNotWritten))
        termios.tcflush(sys.stdin, termios.TCIFLUSH)

