import select
import sys
import termios
import time
from random import choice

nameNotWritten = ["Please write your name?", "Please tell me your name"]
notUnderstood = ["I am sorry, I did not quite understand what you said, what is your name?",
                 "Oh sorry, I did not quite catch that, can you repeat your name?",
                 "Sorry, can you say your name one more time?"]


def askname_func(user):
    termios.tcflush(sys.stdin, termios.TCIFLUSH)
    print("I am Gabriel, what is your name? *")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 30)
        if i:
            sentence = sys.stdin.readline().strip().lower().split(" ")
            if len(sentence) == 1:
                if sentence[0] == "":
                    user.askNameChatbotNotUnderstood += 1
                    print(choice(notUnderstood))
                    continue
                user.name = sentence[0].capitalize()
            elif "the" in sentence:
                index = sentence.index("the")
                user.name = sentence[index + 1].capitalize()
            elif sentence[0] in ["i'm", "im"]:
                user.name = sentence[1].capitalize()
            elif sentence[1] == "name":
                user.name = sentence[3].capitalize()
            elif sentence[1] == "name's":
                user.name = sentence[2].capitalize()
            elif sentence[1] == "am":
                user.name = sentence[2].capitalize()
            else:
                user.askNameChatbotNotUnderstood += 1
                print(choice(notUnderstood))
                continue
            time.sleep(2)
            nameWritten = ["Nice to meet you " + user.name + ", you are a very handsome human",
                           user.name + ", what a lovely name",
                           "It is a pleasure meeting you " + user.name]
            print(choice(nameWritten))
            answered = True
        else:
            user.askNameUserNoResponse += 1
            print(choice(nameNotWritten) + ' *')
    termios.tcflush(sys.stdin, termios.TCIFLUSH)
