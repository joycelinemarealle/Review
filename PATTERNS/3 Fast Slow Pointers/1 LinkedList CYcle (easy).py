class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def has_cycle(head):
    slow ,fast = head,head
    while fast is not None and fast.next is not None:
        slow = slow. next
        fast = fast.next.next
        if slow == fast:
         return True #found cycle
    return False

def main ():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle" + str(has_cycle(head)))

    head.next.next.next.next.next = head.next.next
    print("LinkedList has cycle" + str(has_cycle(head)))

    head.next.next.next.next.next = str(has_cycle(head))

main ()

#specify node
# if cycle then slow and fast pointer will meet
# keep on moving through loop if fast has value and fast  next has value
#slow moves one step from head, fast two steps.  if slow == fast then cycle
#