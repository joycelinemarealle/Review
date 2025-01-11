class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def print_list(self):
        #assign node to temp
        temp = self

        #while node is not empty print out value
        while temp is not None:
            print(temp.value, end = ' ')
            temp = temp.next #move to next node
        print()

def reverse(head):
    #1 Initialization
    previous = None #no nodes reversed yet null
    current = head #start with first node of list
    next = None #temp storage during reversal


    # 2 Iterate over the list
    while current is not None:
        #save the next node so we do not lose the rest of list
        next = current.next

        #reverse current node's next pointer to point to previous
        current.next = previous #reverse current node

        #move previous to current node
        previous = current

        #move current to next node
        current = next
        ''
    return previous

def main ():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    print ("Nodes of original LinkedList are: ", end = '' )
    head.print_list()
    result = reverse(head)
    print("Nodes of traversed LinkedList are: ", end = '')
    result.print_list()


main()