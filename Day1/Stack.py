class Stack:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__top = -1

    def is_full(self):
        if (self.__top == self.__max_size - 1):
            return True
        return False

    def is_empty(self):
        if (self.__top == -1):
            return True
        return False

    def push(self, data):
        if (self.is_full()):
            print("Stack is full")
        else:
            self.__top += 1
            self.__elements[self.__top] = data

    def pop(self):
        if (self.is_empty()):
            print("Stack is empty")
        else:
            data = self.__elements[self.__top]
            self.__top -= 1
            return data

    def display(self):
        if (self.is_empty()):
            print("Stack is empty")
        else:
            index = self.__top
            while (index >= 0):
                print(self.__elements[index], end=" ")
                index -= 1

    def get_max_size(self):
        return self.__max_size


s = Stack(5)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.display()
print()
s.pop()
s.display()