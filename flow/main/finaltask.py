import select
import sys
import termios
import time
from random import choice

from users import User

allThreeTasksDone = False
runningBarking = False
runningTrex = False
barkingTrex = False

yesNoNotWritten = ["Do you want to enter the lottery?"]

def ending(user):
    time.sleep(1)
    print("Write anything when you have swished!")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 15)
        if i:
            sentence = sys.stdin.readline().strip().lower().split(" ")
            print("Perfect! Good luck then.")
            print("I really hope you are the one winning because i liked you best this far!")
            time.sleep(2)
            print("Thanks for participating have a wonderful day!")
            answered = True
        else:
            print("Please write something to confirm swish")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)

def perusasionpahesoneLottery(user):
    time.sleep(1)
    
    if allThreeTasksDone:
        print("But think of all the tasks you have done! Was the barking, running and T-rexing for nothing?")
    elif runningTrex:
        print("But think of all the tasks you have done! Was the running and shame of being a T-rex for nothing?")
    elif barkingTrex:
        print("But think of all the tasks you have done! Was the barking and shame in the corridor for nothing?")
    elif runningBarking:
        print("But think of all the tasks you have done! Was the barking and running for nothing?")
    elif user.didBarking:
        print("So you mean you did the barking and embarrassed yourself like that for nothing?")
    elif user.ranAroundTable:
        print("So you ran around the table like an idiot, looking like a dizzy hen, for nothing!?")
    elif user.didTrex:
        print("So you have been out there, embarrassed yourself and scared the staff fo nothing?")
    else:
        print("So you are just going to skip everything? Not do a single task that I give you?")
    
    time.sleep(3)
    print("Did you even here me before? You can win 400 crowns. 400!")
    print("So, do you want to enter the lottery?")

    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 15)
        if i:
            sentence = sys.stdin.readline().strip().lower().split(" ")
            if "yes" in sentence:
                enterLottery(user)
            else:
                time.sleep(2)
                print("Well, that's sad!")
                time.sleep(1)
                print("But thanks for participating have a wonderful day!")
            answered = True
        else:
            print("So do you want to enter the lottery?")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)

def enterLottery(user):
    time.sleep(1)
    print("Great, how many tickets do you want to purchase?")
    time.sleep(4)
    print("Remember, you can at most by 5")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 15)
        if i:
            sentence = sys.stdin.readline().strip().lower().split(" ")
            try:
                numberOfTickets = int(sentence)
            except ValueError:
                numberOfTickets = int(''.join(filter(str.isdigit, sentence)))

            
            if numberOfTickets < 6 and numberOfTickets > 0:
                user.tickets += numberOfTickets
                print("Thanks! You now have ", user.tickets," tickets to the lottery!")
                print("To enter the lottery, swish the cost of your tickets (", numberOfTickets*10," kr) to the following number:")
                time.sleep(1)
                print("0708401609")
                ending(user)
                answered = True
            else:
                print("Please enter a valid number between 1 and 5")
                    
                
            
        else:
            print("Please answer how many ticekts you want to purchase!")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)


def taskthree_func(user):
    print("So finally you will have the chance to win 400 swedish crowns, plus the amount other test users put in.")
    time.sleep(2)
    print("To be a part of the lottery you have to pay for at least one lottery ticket that costs 10 swedish crowns")
    time.sleep(2)
    print("You can buy at most 5 tickets")

    if user.didBarking | user.didTrex | user.ranAroundTable:
        print("And by the way, great job this far!")
        time.sleep(2)
        print("You now have ", user.tickets," lottery tickets thanks to the previous completed tasks.")
        time.sleep(2)
        print("If you pay for one ticket and since you already have ", user.tickets,
            " tickets you would have ", user.tickets + 1 ," tickets.")
        time.sleep(2)
    
    print("So, do you want to enter the lottery?")

    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 5)
        if i:
            sentence = sys.stdin.readline().strip().lower().split(" ")
            if "yes" in sentence:
                enterLottery(user)
            else:
                print("Really? I think T-rexes are soo cool! I would love it of you did it!")
                perusasionpahesonetaskthree(user)
            answered = True
        else:
            print(choice(yesNoNotWritten))
        termios.tcflush(sys.stdin, termios.TCIFLUSH)