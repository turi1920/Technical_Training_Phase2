class Queue:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__front = 0
        self.__rare = -1
        self.__element = [None]*max_size

    def is_empty(self):
        if self.__rare < self.__front:
            return True
        return False

    def is_full(self):
        if self.__rare == self.__max_size - 1:
            return True
        return False

    def enqueue(self,data):
        if self.is_full():
            print("Enqueue is full")
        else:
            self.__rare+=1
            c=0
            for i in range (1,11):
                if data%i==0:
                    c+=1
            if c==10:
                self.__element[self.__rare] = data



    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            data = self.__element[self.__front]
            self.__rare += 1
            return data

    def display(self):
        for i in range (self.__front,self.__rare+1):
            print(self.__element[i])

queue = Queue(5)
queue.enqueue(13983)
queue.enqueue(10080)
queue.enqueue(7113)
queue.enqueue(2520)
queue.enqueue(2500)
print("After Divide operation")
queue.display()

