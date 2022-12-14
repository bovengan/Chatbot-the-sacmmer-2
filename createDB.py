import sqlite3
from sqlite3 import OperationalError

sqliteConnection = sqlite3.connect('chatbot.db')
cursor = sqliteConnection.cursor()

try:
    cursor.execute("CREATE TABLE Users ("
                   "id text,"
                   "name text,"
                   "age int,"
                   "tickets int,"
                   "didBarking bool,"
                   "ranAroundTable bool,"
                   "didTrex bool,"
                   "moneySpent int,"
                   "askNameUserNoResponse int,"
                   "askNameChatbotNotUnderstood int,"
                   "askAgeUserNoResponse int,"
                   "askAgeChatbotNotUnderstood int,"
                   "askAgeUserNotReady int,"
                   "explanationUserNoResponse int,"
                   "explanationUserNotUnderstood int,"
                   "taskOneUserNoResponse int,"
                   "taskOneUserSayNo int,"
                   "taskTwoUserNoResponse int,"
                   "taskTwoUserSayNo int,"
                   "taskThreeUserNoResponse int,"
                   "taskThreeUserSayNo int,"
                   "taskFinalUserNoResponse int,"
                   "taskFinalUserSayNo int,"
                   "userNoResponse int)")
    sqliteConnection.commit()
    print('New table created')
except OperationalError:
    print('Table already exists')
sqliteConnection.commit()
sqliteConnection.close()