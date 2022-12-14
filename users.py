import sqlite3

sqliteConnection = sqlite3.connect('chatbot.db')
cursor = sqliteConnection.cursor()
cursor.execute("SELECT * FROM Users")
numberOfParticipants = str(len(cursor.fetchall()))
sqliteConnection.commit()
sqliteConnection.close()


class User:

    def __init__(self, name=None, age=None, tickets=0):
        self.id = "C" + numberOfParticipants
        self.name = name
        self.age = age
        self.tickets = tickets
        self.didBarking = False
        self.ranAroundTable = False
        self.didTrex = False
        self.moneySpent = 0

        # askname
        self.askNameUserNoResponse = 0
        self.askNameChatbotNotUnderstood = 0

        # askage
        self.askAgeUserNoResponse = 0
        self.askAgeChatbotNotUnderstood = 0
        self.askAgeUserNotReady = 0

        # explanation
        self.explanationUserNoResponse = 0
        self.explanationUserNotUnderstood = 0

        # taskone
        self.taskOneUserNoResponse = 0
        self.taskOneUserSayNo = 0 # inte i databasen

        # tasktwo
        self.taskTwoUserNoResponse = 0
        self.taskTwoUserSayNo = 0 # inte i databasen

        # taskthree
        self.taskThreeUserNoResponse = 0
        self.taskThreeUserSayNo = 0 # inte i databasen

        # taskfinal
        self.taskFinalUserNoResponse = 0
        self.taskFinalUserSayNo = 0

        # total
        self.userNoResponse = self.askNameUserNoResponse + \
                              self.askAgeUserNoResponse + \
                              self.explanationUserNoResponse + \
                              self.taskOneUserNoResponse + \
                              self.taskTwoUserNoResponse + \
                              self.taskThreeUserNoResponse + \
                              self.taskFinalUserNoResponse
