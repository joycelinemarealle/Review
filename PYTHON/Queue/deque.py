from collections import deque
# q = deque()
# q.appendleft(5)
# q.appendleft(6)
# q.appendleft(7)

# print(q)
# print(q.pop())
# print(q.pop())
# print(q.pop())


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

if __name__ == '__main__':
    pq = Queue()

    #add values in queue
    pq.enqueue(
        {'company': 'Wal Mart',
         'timestamp' : '15 apr, 11.01 AM',
         'price' :131.10
        }
    )

    pq.enqueue(
        {'company': 'Wal Mart',
         'timestamp': '15 apr, 11.02 AM',
         'price': 132
         }
    )

    pq.enqueue(
        {'company': 'Wal Mart',
         'timestamp' : '15 apr, 11.03 AM',
         'price' :135
        }
    )

    print(pq.buffer)
    print(pq.dequeue())
    print(pq.size())