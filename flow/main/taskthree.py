import select
import sys
import termios
import time
from random import choice

from users import User

yesNoNotWritten = ["I didn't quite hear you. Soo do you want scare the people working out there?"+ 
"Do you want to pretend to be a T-rex?", "One more time. Do you want to be a T-rex?"]

def trytaskthree(user):
    time.sleep(1)
    print("Marvelous, I knew you would do it! Don't scare me to much now though!"+
    "But just go out and start whenever you are ready!")
    time.sleep(4)
    print("Answer yes or no if the task leaders informed you that you completed the task or not")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 15)
        if i:
            sentence = sys.stdin.readline().strip().lower().split(" ")
            if "yes" in sentence:
                print("HELP, do not come closer! I am convinced you are a T-rex now!")
                print("Oh sorry, i lost it again! But well done i guess! Lets move on to the final task!")
            else:
                print(
                    "Well, well, well, well. Valid effort but not nearly good enough!"
                    + "That's an F for this task, but let's move on to the final!")
                
            answered = True
        else:
            print("Please answer yes or no")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)

def perusasionpahesonetaskthree(user):
    time.sleep(1)
    print("This can be epic! Think about it!")
    if user.didBarking & user.ranAroundTable:
        print("You already barked, and ran around this table...")
        print("This is not any worse than that, right?")
    elif user.didBarking:
        print("You already barked like a mad dog!")
        print("The damage is already done, this is not worse, right?")
    elif user.ranAroundTable:
        print("You have already been up and running!")
        print("Think of this as an extension of that!")
    print("So do you want to do the T-rex?")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 15)
        if i:
            sentence = sys.stdin.readline().strip().lower().split(" ")
            if "yes" in sentence:
                trytaskthree(user)
            else:
                print("Okay, okay! You are a scared i guess!")
                print("Lets move on to the final task instead!")
            answered = True
        else:
            print("So do you want to try it?")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)

def taskthree_func(user):
    print("Okay, so wouldn't it be fun if you now go out in the corridor and pretend that you are the dinosaur T-rex?")
    time.sleep(2)
    print("And you should both look like one and sound like a T-rex! That would be awesome!")
    time.sleep(2)
    print("So is this something for you?")

    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 5)
        if i:
            sentence = sys.stdin.readline().strip().lower().split(" ")
            if "yes" in sentence:
                trytaskthree(user)
            else:
                print("Really? I think T-rexes are soo cool! I would love it of you did it!")
                perusasionpahesonetaskthree(user)
            answered = True
        else:
            print(choice(yesNoNotWritten))
        termios.tcflush(sys.stdin, termios.TCIFLUSH)




