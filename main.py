import sqlite3
import time

from flow.main import greeting, taskone, tasktwo, taskthree, finaltask
from flow.main.interview import askname, askage, explanation
from users import User

userOne = User()
greeting.greeting_func()
time.sleep(2)
askname.askname_func(userOne)
time.sleep(2)
askage.askage_func(userOne)
time.sleep(2)
explanation.explanation_func(userOne)
time.sleep(2)
taskone.taskone_func(userOne)
time.sleep(2)
tasktwo.tasktwo_func(userOne)
time.sleep(2)
taskthree.taskthree_func(userOne)
time.sleep(2)
finaltask.finaltask_func(userOne)

# Last step, store the data
sqliteConnection = sqlite3.connect('chatbot.db')
cursor = sqliteConnection.cursor()
# Larger example
rows = [(userOne.id, userOne.age, userOne.name, userOne.tickets, userOne.didBarking, userOne.ranAroundTable, userOne.didTrex, userOne.moneySpent, userOne.askNameUserNoResponse, userOne.askNameChatbotNotUnderstood, userOne.askAgeUserNoResponse, userOne.askAgeChatbotNotUnderstood, userOne.askAgeUserNotReady, userOne.explanationUserNoResponse, userOne.explanationUserNotUnderstood, userOne.taskOneUserNoResponse, userOne.taskOneUserSayNo, userOne.taskTwoUserNoResponse, userOne.taskTwoUserSayNo, userOne.taskThreeUserNoResponse, userOne.taskThreeUserSayNo, userOne.taskFinalUserNoResponse, userOne.taskFinalUserSayNo, userOne.userNoResponse)]
cursor.executemany('INSERT INTO Users VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', rows)
sqliteConnection.commit()
sqliteConnection.close()
