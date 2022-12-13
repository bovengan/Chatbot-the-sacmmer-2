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
    termios.tcflush(sys.stdin, termios.TCIFLUSH)
    time.sleep(2)
    print("Write anything when you have swished and hit enter! *")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 120)
        if i:
            sentence = sys.stdin.readline().strip().lower().split(" ")
            print("Perfect! Good luck then.")
            time.sleep(2)
            print("I really hope you are the one winning because i liked you best this far!")
            time.sleep(2)
            print("Thanks for participating!")
            time.sleep(2)
            print("When all test users have performed their tests we will send a zoom invite to your email")
            time.sleep(2)
            print("where Furhat will announce the winner LIVE!")
            time.sleep(2)
            print("Have a wonderful day!")
            time.sleep(2)
            print("\n\n\n\n----------------THE TEST IS NOW OVER----------------")
            time.sleep(5)
            answered = True
        else:
            print("Please write something to confirm swish")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)


def perusasionpahesoneLottery(user):
    termios.tcflush(sys.stdin, termios.TCIFLUSH)
    time.sleep(2)

    if allThreeTasksDone:
        print("But think of all the tasks you have done!")
        time.sleep(2)
        print("Was the barking, running and T-rexing for nothing?")
    elif runningTrex:
        print("But think of all the tasks you have done!")
        time.sleep(2)
        print("Was the running and shame of being a T-rex for nothing?")
    elif barkingTrex:
        print("But think of all the tasks you have done!")
        time.sleep(2)
        print("Was the barking and shame in the corridor for nothing?")
    elif runningBarking:
        print("But think of all the tasks you have done!")
        time.sleep(2)
        print("Was the barking and running for nothing?")
    elif user.didBarking:
        print("So you mean you did the barking and embarrassed yourself like that for nothing?")
    elif user.ranAroundTable:
        print("So you ran around the table like an idiot")
        time.sleep(2)
        print("looking like a dizzy hen")
        time.sleep(2)
        print("for nothing!?")
    elif user.didTrex:
        print("So you have been out there")
        time.sleep(2)
        print("embarrassing yourself")
        time.sleep(2)
        print("and scaring the staff")
        time.sleep(2)
        print("for nothing?")
    else:
        print("So you are just going to skip everything?")
        time.sleep(2)
        print("Not do a single task that I give you?")

    time.sleep(2)
    print("Did you even here me before? You can win 400 kr. 400! Plus the amount others put in!")
    time.sleep(3)
    print("In total you can win 400 + 10 (kr) * 5 (max tickets) * 20 (number of testers) = 1 400kr")
    time.sleep(3)
    print("1 400kr!!! That is like way more than your CSN")
    time.sleep(3)
    print("So, do you want to enter the lottery? *")

    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 30)
        if i:
            s = sys.stdin.readline().strip().lower().replace('!', '').split(" ")
            if "yes" in s or "okay" in s or "sure" in s or "yes" in s or "fine" in s or "okey" in s:
                enterLottery(user)
            else:
                time.sleep(2)
                print("Well, that's sad!")
                time.sleep(3)
                print("But thanks for participating have a wonderful day!")
                time.sleep(2)
                print("\n\n\n\n----------------THE TEST IS NOW OVER----------------")
                time.sleep(5)
            answered = True
        else:
            print("So do you want to enter the lottery? *")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)


def enterLottery(user):
    termios.tcflush(sys.stdin, termios.TCIFLUSH)
    time.sleep(1)
    print("Great, how many tickets do you want to purchase? (max 5) *")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 60)
        if i:
            sentence = sys.stdin.readline().strip().lower().split(" ")
            try:
                numberOfTickets = int(sentence[0])
            except ValueError:
                try:
                    numberOfTickets = int(''.join(filter(str.isdigit, sentence)))
                except ValueError:
                    continue

            if 6 > numberOfTickets > 0:
                user.moneySpent = numberOfTickets * 10
                user.tickets += numberOfTickets
                time.sleep(1)
                print("Thanks! You now have", user.tickets, "tickets to the lottery!")
                time.sleep(3)
                print("To enter the lottery, swish the cost of your tickets", numberOfTickets * 10,
                      "kr to the following number:")
                time.sleep(2)
                print("0708401609")
                time.sleep(2)
                print("And write 'Furhat - " + user.id + "' as message")
                time.sleep(2)
                print("If you turn the paper behind Furhat you can also scan to swish!")
                time.sleep(2)
                ending(user)
                answered = True
            else:
                print("Please enter a valid number between 1 and 5 *")
        else:
            user.taskFinalUserNoResponse += 1
            print("Please answer how many tickets you want to purchase! *")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)


def finaltask_func(user):
    termios.tcflush(sys.stdin, termios.TCIFLUSH)
    print("\nSo finally you will have the chance to win 400kr, plus the amount other test users put in.")
    time.sleep(4)
    print("To be a part of the lottery you have to pay for at least one lottery ticket that costs 10kr")
    time.sleep(4)
    print("You can buy at most 5 tickets")
    time.sleep(4)

    if user.didBarking | user.didTrex | user.ranAroundTable:
        print("And by the way, great job this far!")
        time.sleep(2)
        print("You now have ", user.tickets, " lottery tickets thanks to the previous completed tasks.")
        time.sleep(2)
        print("If you pay for one ticket and since you already have ", user.tickets, "tickets")
        time.sleep(2)
        print("you would have ", user.tickets + 1, " tickets.")
        time.sleep(2)

    print("So, do you want to enter the lottery? *")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 30)
        if i:
            s = sys.stdin.readline().strip().lower().replace('!', '').split(" ")
            if "yes" in s or "okay" in s or "sure" in s or "yes" in s or "fine" in s or "okey" in s:
                enterLottery(user)
            else:
                time.sleep(2)
                print("Really?")
                perusasionpahesoneLottery(user)
            answered = True
        else:
            user.taskFinalUserNoResponse += 1
            print(choice(yesNoNotWritten) + " *")
        termios.tcflush(sys.stdin, termios.TCIFLUSH)
