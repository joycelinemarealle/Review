class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def has_cycle(head):
    cycle_length = 0
    #two pointer to see if cycle exists
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: #found cycle
            cycle_length = calculate_cycle_length(slow)
            break
    return find_start(head, cycle_length)

def calculate_cycle_length(slow):
    #calculate length of cycle. Start from where slow and fast meet
    cycle_length = 0
    current = slow
    while True:
        current = current.next
        cycle_length += 1

        if current == slow:
            break
    return cycle_length

def find_start(head, cycle_length):
    pointer1, pointer2 = head, head

    #move pointer ahead by K nodes
    while cycle_length >0:
        pointer2 = pointer2.next
        cycle_length -= 1

    #increemtn both pointer2 and pointer2 until they meet at start of cycle
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


def main ():
    head = Node (1)
    head.next = Node(2)
    head.next.next = Node (3)
    head.next.next.next= Node (4)
    head.next.next.next.next = Node (5)
    head.next.next.next.next.next = Node (6)
    head.next.next.next.next.next = head.next.next
    print ("Linked list cycle start: " + str(has_cycle(head).value))

main()