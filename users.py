class User:

    def __init__(self, name=None, age=None, tickets=0):
        self.name = name
        self.age = age
        self.tickets = tickets
        self.didBarking = False
        self.ranAroundTable = False
        self.didTrex = False

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

        # tasktwo
        self.taskTwoUserNoResponse = 0

        # taskthree
        self.taskThreeUserNoResponse = 0

        # taskfinal
        self.taskFinalUserNoResponse = 0

