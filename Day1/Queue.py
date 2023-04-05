class Queue:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__rear = -1
        self.__front = 0

    def is_full(self):
        if (self.__rear == self.__max_size - 1):
            return True
        return False

    def is_empty(self):
        if (self.__front > self.__rear):
            return True
        return False

    def enqueue(self, data):
        if (self.is_full()):
            print("\nQueue is full")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data
            # print("Element pushed")

    def dequeue(self):
        if (self.is_empty()):
            print("Queue is empty")
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data

    def display(self):
        if (self.is_empty()):
            print("Queue is empty")
        else:
            index = self.__front
            while (index <= self.__rear):
                print(self.__elements[index], end=" ")
                index += 1

    def get_max_size(self):
        return self.__max_size


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
            print("Element pushed")

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


q = Queue(7)
s = Stack(10)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.display()
print()
q.dequeue()
q.enqueue(9)
q.display()
