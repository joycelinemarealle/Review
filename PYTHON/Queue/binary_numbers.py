from collections import deque
import time


class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self,val): #insert in queue
        self.buffer.appendleft(val)

    def dequeue(self): #remove from queue
       return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]

def produce_binary_numbers(n):
    numbers_queue = Queue()
    #add to queue 1 as str
    numbers_queue.enqueue("1")

    #loop through numbers print front number and add 1 +0

    for i in range(n):
        #get 1 front number
        front = numbers_queue.front()
        print("  ", front)

        #concatenate front with 0 and 1 and add to queue
        numbers_queue.enqueue((front) + "0")
        numbers_queue.enqueue((front) + "1")

       #remove first number so, second number used in the loop
        numbers_queue.dequeue()

if __name__ == '__main__':
    produce_binary_numbers(4)
