class queueH:
    def __init__(self):
        self.list = []

    def enqueue(self,call):
        self.list.append(call)

    def dequeue(self):
        self.list.pop(0)

    def peek(self):
        return self.list[0]

class stack:
    def __init__(self):
        self.list = []

    def push(self,call):
        self.list.append(call)

    def pop(self):
        self.list.pop(len(self.list)-1)

    def peek(self):
        return self.list[len(self.list)-1]

class call:
    def __init__(self,callerId,time_received):
        self.callerId = callerId
        self.time_received = time_received