class patient:
    def __init__(self,name,appointment_date):
        self.name = name
        self.appontment = appointment_date

class queueH:
    def __init__(self):
        self.list = []

    def enqueue(self,patient):
        self.list.append(patient)

    def dequeue(self):
        self.list.pop(0)

    def peek(self):
        return self.list[0]