
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def print_list(self):
        #save node
        temp = self
        #loop through list
        while temp is not None:
            print(temp.value, end = ' ')
            #move to next node
            temp = temp.next
        print()

def reverse_every_k_elements(head, k):
    #1 Base case. No need to reverse since one element does nothing
    if k<=1 or head is None:
        return head
    # 2 Loop through the linked list
    current, previous, next,  = head, None, None
    #next temp store next node will reversing pointers
    while True: #process 1 k group at a time
        #3 Save pointers
        last_node_of_previous = previous
        # after reversing the linkedlist 'current' will become the last node of sublist
        last_node_of_sublist = current

        #4 Reverse sublist
        i = 0
        while current is not None and i< k:
            #save next
             next = current.next
            #reverse pointer to previous
             current.next = previous
            #previous pointer is on current node
             previous = current
            #move to next node
             current = next
             i+=1

         #5 Connect with previous part
        if last_node_of_previous is not None:
         last_node_of_previous.next = previous
        else:
         head = previous

        # 6 connect with next part
        last_node_of_sublist.next = current

        # 7 Break condition
        if current is None: #reached end of list exit loop
             
            break
        previous = last_node_of_sublist
    return head




def main ():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next = Node(6)
