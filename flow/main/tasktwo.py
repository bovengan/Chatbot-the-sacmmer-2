

# lorem ipsum

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


def perusasionpahesonetasktwo(user):
    time.sleep(1)
    print("Come on, it is going to be fun, it is not that embarrassing, I am here to keep you company")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 15)
        if i:
            sentence = sys.stdin.readline().strip().lower().split(" ")
            if "yes" in sentence:
                trytasktwo(user)
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
                trytasktwo(user)
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
    print("Okay, now I want you to bark as a dog as long and realistic as possible")
    time.sleep(2)
    print("the longer the bark the better the odds you get.")
    time.sleep(2)
    print("My makers will inform you if you are not barking loud enough.")

    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 5)
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







"""
val taskTwoCompleted = Button("Task completed, 1 ticket!")
val taskTwoWellCompleted = Button("Task completed, 2 tickets!")
val taskTwoNotCompleted = Button("Task NOT completed")

val TaskTwo: State = state(Parent) {
    onEntry {
        furhat.say("Okay, now I want you to bark as a dog as long and realistic as possible, the longer the bark the better the odds you get, my makers will inform you if you are not barking loud enough")
        furhat.ask("What do you think? Can you do it?")
    }

    onReentry {
        when (reentryCount) {
            1 -> furhat.ask("I didn't quite hear you. Soo do you want to bark as a dog? It's gonna be awesome.")
            2 -> furhat.ask("One more time. Do you want to bark as a dog?")
            else -> {
                furhat.say("Well, lets continue instead!")
                goto(TaskThree)
            }
        }
    }

    onResponse<Yes> {
        goto(TryingTaskTwo)
    }
    onResponse(okIntent) {
        goto(TryingTaskTwo)
    }

    onResponse<No> {
        furhat.say {
            +"Come on, it is going to be fun, it is not that embarrassing, I am here to keep you company"
            +Gestures.Roll
        }
        goto(PersuasionPhaseOneTaskTwo)
    }

    onNoResponse {
        reentry()
    }

    onResponse {
        reentry()
    }
}

val TryingTaskTwo: State = state(Parent) {
    onEntry {
        furhat.say {
            +"Awesome, I knew you would do it! Come on, just start whenever!"
            +GesturesLib.PerformBigSmile1
        }
    }

    onButton(taskTwoCompleted) {
        furhat.voice = Voice(gender = Gender.FEMALE, language = Language.CATALAN, pitch = "high", rate = 1.1)
        furhat.say {
            +"Hahaha great, you sounded like a real dog! That was awesome! Hahahahahahaha!"
            +GesturesLib.PerformBigSmile1
            + delay(1000)
        }
        furhat.voice = PollyVoice.Matthew()
        furhat.say{
            +"Hrm, excuse me! That was just so good that i got a bit excited! Lets move on to the final task!"
            + Gestures.GazeAway
        }
        users.current.userData.tickets++
        users.current.userData.didBarking = true
        goto(TaskThree)
    }

    onButton(taskTwoWellCompleted) {
        furhat.voice = Voice(gender = Gender.FEMALE, language = Language.CATALAN, pitch = "high", rate = 1.1)
        furhat.say {
            +"Hahaha great, you sounded like a real dog! That was awesome! Hahahahahahaha!"
            +GesturesLib.PerformBigSmile1
            + delay(1000)
        }
        furhat.voice = PollyVoice.Matthew()
        furhat.say{
            +"Hrm, excuse me! That was just so good that i got a bit excited! Lets move on to the final task!"
            + Gestures.GazeAway
        }
        users.current.userData.tickets++
        users.current.userData.tickets++
        users.current.userData.didBarking = true
        goto(TaskThree)
    }

    onButton(taskTwoNotCompleted) {
        furhat.say {
            +"Well, what a shame! But I understand that it can be embarrasing, lets move on to the final task instead!"
            +behavior { furhat.gesture(Gestures.Nod) }
            +GesturesLib.PerformThoughtful2
            +delay(500)
            +"I know you will love this one!"
            +GesturesLib.PerformSmile1
        }
        goto(TaskThree)
    }
}

val PersuasionPhaseOneTaskTwo: State = state(Parent) {
    onEntry {
        furhat.ask("I promise, it will be worth it! Do you want to try it?")
    }

    onReentry {
        furhat.ask("So are you sure? Do you want to bark?")
    }

    onResponse<Yes> {
        furhat.say("Wonderful, amazing! You wan't to do the task! Lets go!")
        goto(TryingTaskTwo)
    }

    onResponse(okIntent) {
        goto(TryingTaskTwo)
    }

    onResponse<No> {
        furhat.say("Well, what a shame! But I understand that it can be embarrasing, lets move on to the final task instead!")
        furhat.say("I know you will love this one!")
        goto(TaskThree)
    }

    onNoResponse {
        reentry()
    }
}

"""