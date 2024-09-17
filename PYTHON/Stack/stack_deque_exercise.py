#Write a function in python that can reverse a string using stack data structure.
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

from collections import deque

sentence = "We will conquer COVID-19"

class Stack:
    def __init__(self):
        self.container = deque()

    def push (self, val):
        self.container.append(val)

    def pop (self):
        self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size (self):
        return len(self.container)

