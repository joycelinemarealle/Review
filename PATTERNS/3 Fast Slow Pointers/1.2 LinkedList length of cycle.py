class Node :
    def __init__ (self, value, next = None):
        self.value = value
        self.next = next

def find_cycle_length(head):
    slow,fast = head,head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return calculate_cycle_length(slow)
    return False

def calculate_cycle_length(slow):
    #save slow pointer
    cycle_length = 0
    current = slow
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length
    #iterate using another pointer
#track length until slow == current pointer
def main ():
    head = Node(1)
    head.next = Node (2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node (5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has a Cycle length: " + str(find_cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print ("Linked cycle length:" + str(find_cycle_length(head)))
main ()