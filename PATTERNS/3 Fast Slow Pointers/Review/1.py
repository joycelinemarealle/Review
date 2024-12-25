class Node:
    def __init__ (self,value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    slow,fast = head,head
    while fast is not None and fast.next is not None:
        fast = slow.next.next #fast pointer
        slow = slow.next #slow pointer
        if slow == fast: #found cycle
         return True
    return False

# 1-> 2-> 3-> 4-> 5->6-> merges to 3
def main ():
    head = Node (1)
    head.next = Node (2)
    head.next.next = Node (3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head.next.next #creates a cycle by pointing back to Node(3)
    print ( "LinkedList had a cycle " + str ( has_cycle(head) ))

main()

#slow and fast pointers, fast goes twice as slow
# the fast will go through the linkedlist and at some point meet the slow pointer. The fast goes till the end and lops back in
#if the fast and slow do not meet it means there is no cycle
    #is if fast is one step behind the slow--- they will at the next itieration
    # if fast two steps before the slow, then the next iteration (scenario) one. so will meet at next next iteration

    #create node class
    #create nodes
    #has a cycle
        #both pointers starting from head
        #fast twice as slow
        #while fast i not nne or next is none
            #if slow == fast
            #return True