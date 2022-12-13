import select
import sys
import termios
import time

from users import User


def understand():
    print("Okay so what is going to happen now is that I am going to give you 3 tasks I want you to perform.")
    time.sleep(3)
    print("You do not have to do them, but if you do you will get points that will increase your odds of winning a gift from my makers.")
    time.sleep(3)
    print("I will be the judge, with a bit of assistance from my makers, if you complete the tasks or not.")
    time.sleep(3)
    print("Do you understand?" + ' *')


def explanation_func(user):
    termios.tcflush(sys.stdin, termios.TCIFLUSH)
    understand()
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 50)
        if i:
            s = sys.stdin.readline().strip().lower().replace('!', '').split(" ")
            if "yes" in s or "okay" in s or "sure" in s or "yes" in s or "fine" in s or "okey" in s:
                termios.tcflush(sys.stdin, termios.TCIFLUSH)
                answered = True
            else:
                termios.tcflush(sys.stdin, termios.TCIFLUSH)
                user.explanationUserNotUnderstood += 1
                print("Hmm okay, that might have been a long instruction.")
                time.sleep(2)
                explanationAnswer = input("Do you want me to simplify? Or maybe explain it in Japanese? *\n").strip().lower().replace('!', '').split(" ")
                if "no" in explanationAnswer:
                    print("Great, let's continue")
                    answered = True
                else:
                    if "simplify" in explanationAnswer:
                        print("You will get three tasks to complete")
                        time.sleep(1)
                        print("for each completed task you get better odds at winning the gift.")
                        time.sleep(1)
                        print("Let's continue...")
                        answered = True
                    elif "japanese" in explanationAnswer:
                        time.sleep(1)
                        print("完了するタスクが 3 つあり、完了したタスクごとに、ギフトを獲得する確率が高くなります。ここで最初のタスクです")
                        time.sleep(3)
                        print("Just kidding. That would have been cool though")
                        time.sleep(2)
                        answer = input("So, do you understand what you are going to do? *\n").strip().lower().split(" ")
                        if "yes" not in answer:
                            user.explanationUserNotUnderstood += 1
                            time.sleep(2)
                            understand()
                        else:
                            answered = True
        else:
            user.explanationUserNoResponse += 1
            print("Please type yes or no if you understand *")

#explanation_func(User(1, 2, 3))
