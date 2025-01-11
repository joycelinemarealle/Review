class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def print_list(self):
        #save the node
        temp = self

        #loop through list
        while temp is not None:
            print(temp.value, end = ' ')
            #move to next node
            temp = temp.next
        print()

def reverse_sublist(head, p,q):
    #1 base case
    if p== q:
        return head
    # 2 Skip the first p-1 nodes to reach to node at position p
    current, previous = head, None
    i = 0
    #loop moves current pointer to pth position(start of the range to reverse
    while current is not None and i < p-1:
        previous = current #keeps track of node before
        current = current.next
        i +=1

    # 3 Save pointers
    #the node before p. use this to connect later
    last_node_of_previous_part = previous

    #after reversing sublist the current will now be at the last position. so save it now
    last_node_of_sub_list = current

    # 4 Reverse nodes between p and q
    i = 0
    #after loop previous points to head of reversed sublist and current point to node after q
    while current is not None and i < q-p+1:
       #save the next value
       next = current.next

       #reverse pointer to previous
       current.next = previous

       #previous is now current
       previous = current

       #move to next node
       current = next
       i+=1

    #5 Connect the reversed section
    if last_node_of_previous_part is not None:
        #p > 1 previous is noe the first node of the sublist
        last_node_of_previous_part.next = previous #pointer to head of reversed sublist

        # p==1 we are changing firs tnode of linkedlist. since last node_of_previous = none
    else:
        head = previous

    #6 Connect with last part
    last_node_of_sub_list.next = current
    return head

def main ():
    head = Node(1)
    head.next = Node (2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print ("node of original reversal")

    head.print_list()
    result = reverse_sublist(head,2,4)
    result.print_list()

main ()