#determine if there is a cycle
#if there is then length of the cycle
#if cycle fast + slow pointers will meet at some point == cycle
#when they meet save the slow pointer , then keep track of counts until the slow pointer is reached

class Node:
    def __init__(self, value, next = None):
        self.next = next
        self.value = value

def find_length_of_cycle(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return calculate_length_cycle(slow)
    return 0

def calculate_length_cycle(slow):
    length_cycle = 0
    current = slow
    while True:
        current = current.next
        length_cycle += 1
        if current == slow:
            break
    return length_cycle

def main ():
    head = Node (1)
    head.next = Node (2)
    head.next.next = Node (3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next = head.next.next
    print("The length of the cycle is " + str(find_length_of_cycle(head)))

main()