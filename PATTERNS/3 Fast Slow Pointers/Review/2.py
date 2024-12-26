class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
        
def find_cycle_start(head):
    cycle_length = 0
    slow, fast = head, head
    while fast is not None and fast.next is not None: #loop as long as fast node is not none or the next is not
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            cycle_length = calculate_length_of_cycle(slow)
            break
    return find_start(head,cycle_length)

def calculate_length_of_cycle(slow):
    cycle_length= 0
    current = slow
    while True:
        current = current.next #itierate through cycle
        cycle_length+=1 #keep track of counts to get length
        if slow == current: 
            break #brean loop then return counts == lenght of cycle
        return cycle_length

def find_start(head, cycle_length):
    #two pointers start at same point
    pointer1 , pointer2 = head, head

    #move pointer2 by the cycle length?
    while cycle_length > 0:
        pointer2=pointer2.next
        cycle_length -=1

    #the incremental until two pointers meet
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

        
        
    return False

def main ():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node (5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next = head.next.next
    
main()


#two pointer, slow + fast ()
#determine is a cycle (fast + slow == meet at point 
#determine length of cycle ( from the point the two pointer meet until slow pointer appear again)
#determine start of the node
 #fast pointer move length of cylce
 #incremental both pointers
 #next time they meet will be at the start of cycle
 
 