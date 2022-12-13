class User:

    def __init__(self, name=None, age=None, tickets=0):
        self.name = name
        self.age = age
        self.tickets = tickets
        self.didBarking = False
        self.ranAroundTable = False
        self.didTrex = False

        # askname
        self.askNameNotUnderstood = 0

        # askage
        self.askAgeChatbotNotUnderstood = 0
        self.askAgeUserNotReady = 0

        # explanation
        self.explanationUserNoResponse = 0
        self.explanationUserNotUnderstood = 0

        # taskone
        self.taskOneUserNoResponse = 0

        # tasktwo
        self.taskTwoUserNoResponse = 0

        # tasktwo
        self.taskThreeUserNoResponse = 0

