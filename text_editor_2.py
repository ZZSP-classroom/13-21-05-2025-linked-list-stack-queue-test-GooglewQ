class stack:
    def __init__(self):
        self.list = []

    def push(self,operation):
        self.list.append(operation)

    def pop(self):
        self.list.pop(len(self.list)-1)

    def peek(self):
        return self.list[len(self.list)-1]