
class Node:
    def __init__ (self, value , next = None):
        self.next = next
        self.value = value

    def print_list (self):
        #save current node
        temp = self

        #loop through linkedlist
        while temp is not None:
            print(temp.value, end =' ')
            #move to next node
            temp = temp.next
        print()
def reverse_linkedlist(head):

    # 1 Initialization
    previous = None
    current = head
    next = None

     #Iterate over the list
    while current is not None:
        #save next node
        next = current.next

        #reverse pointer of current node
        current.next = previous

        #previous to curent node
        previous = current

        #move to next node
        current = next
    return previous

def main ():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next =  Node(8)
    head.next.next.next.next = Node(10)
    print ( "node of original linkedlist: ")
    head.print_list()
    print("node of traversed linkedlist:")
    result = reverse_linkedlist(head)
    result.print_list()

main()
# 1-> 2->3 -> 4 reverse to 4-> 3-> 2-> 1
#single node points to next element
#given head == first element/node
#return new head of reversed

#head points to node (2), prev is none
#reverse current node points to prev,  and prev points to current node

#prev is none and current
#loop through node
# reverse current node pointer to prev + prev points to current node
#move to next node