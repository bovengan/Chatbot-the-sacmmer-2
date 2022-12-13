import sqlite3
import time

from flow.main import greeting, taskone
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
print("done so far")

# Last step, store the data
sqliteConnection = sqlite3.connect('chatbot.db')
cursor = sqliteConnection.cursor()
userId = hash(User.name)
userAge = User.age
userTickets = User.tickets
cursor.execute("INSERT INTO Users VALUES (userId, userAge, userTickets)")
sqliteConnection.commit()
sqliteConnection.close()
