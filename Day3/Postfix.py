class Evaluate:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.array = []

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def peek(self):
        return self.array[-1]

    def pop(self):
        if self.isEmpty():
            return '$'
        else:
            self.top -= 1
            return self.array.pop()

    def push(self, data):
        self.top += 1
        self.array.append(data)

    def evalPostfix(self, exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                x = self.array.pop()
                y = self.array.pop()
                self.push(str(eval(x + i + y)))
        return int(self.pop())


exp = "231*+9-"
obj = Evaluate(len(exp))
print(obj.evalPostfix(exp))
