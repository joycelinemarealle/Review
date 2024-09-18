import time
from collections import deque
import threading

#threads
#t1 place order time delay 0.5
#t2 serve order

dq = deque()

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

def place_order(orders):
    for order in orders:
        print('Placing order for', order)
        dq.appendleft(order)
        time.sleep(0.5)


def serve_order(n):
    while len(dq) > 0:
        order = dq.pop()
        print('Serving', order)
        time.sleep(2)

if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t = time.time()
    t1 = threading.Thread(target = place_order, args = (orders,))
    t2 = threading.Thread(target = serve_order, args = (orders,))

    #start threads
    t1.start()
    t2.start()

    #join threads to main
    t1.join()
    t2.join()

    print('done in : "', time.time()-t)

    # go through order list and append left to deque
    # time sleep
    # print
