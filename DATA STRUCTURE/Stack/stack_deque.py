from collections import deque
# stack = deque()
# #print(dir(stack))
# stack.append(5)
# stack.append(10)
# stack.append(15)
# print(stack)

class Stack:
    def __init__(self):
        self.container = deque()

    def push (self, val):
        self.container.append(val)

    def pop(self):
        self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


if __name__ == '__main__':
    s = Stack()
    s.push(5)
    s.push(10)
    s.push(15)
    print(s.peek())
    s.pop()
    print(s.peek())
    print(s.container)
    s.push(67)
    s.push(7)
    s.push(345)
    print(s.size())
    print(s.container)
