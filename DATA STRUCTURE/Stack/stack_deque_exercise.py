#Write a function in python that can reverse a string using stack data structure.
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push (self, val):
        self.container.append(val)

    def pop (self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size (self):
        return len(self.container)


def reverse_string(s):
    #s a string
        stack = Stack ()

        for char in s:
            stack.push(char)

        rstr = ''
        while stack.size()!=0: #stack not empty
            rstr += stack.pop()
        return rstr

#push the word
#then have empty dequer
#split sentence into letters
#letter popped added to this new deque
#print deque


#2 Write a function in python that checks if parenthesis in the string are balanced or not.
# Possible parantheses are "{}',"()" or "[]".

#go through each element in a sentence
#check for all types of parenthiss
#for each type check if even then return true
#if not even return false




def is_balanced(s):
    stack = Stack()
    match_dict = {
        '{': '}',
        '[': ']',
        '(': ')'}
   #loop through string
    for char in s:
        if char in '{([': #if character opening bracket push it to stack
            stack.push(char)
        elif char in ' })]': #if it is closing brackets
            if stack.size() ==0 or  match_dict[stack.pop()] != char:
                return False #unbalanced brackets
    #stack is now empty and all parenthesis balanced
    return stack.size() ==0



if __name__ == '__main__':
    print(reverse_string('We will conquere COVID-19'))
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
