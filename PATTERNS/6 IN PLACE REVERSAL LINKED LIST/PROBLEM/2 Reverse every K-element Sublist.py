class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self

        #as long as node is not empty keep printing value
        while temp is not None:
            print(temp.value, end = '')
            #move to next node
            temp = temp.next

def reverse_every_k_elements(head, k):
    #edge cases
    #if sublist size required <=1 or node empty
    if k <=1 or head is None:
        return head

    # 1 Initialization pointers
    current, previous = head, None

    # 2
    # Outer loop  make sure every node is processed
    while True:
        #pointer keeps track of last node in already processes part of list. first will point to none
        last_node_of_previous_part = previous

        #after reversing the Linkedlist 'current' will become last node of sublist,
        # after reversing sublist last node tracked to connect to next node

        last_node_sub_list = current

        next = None #will be used to temporarily store the next node

    #Inner loop reverse sublist
        i = 0
        while current is not None and i < k: #reverse 'k' nodes
            next = current.next
            previous = current
            current = next
            i+=1

        #connect with previous part
        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = previous #current where sublist ends. new head of reversed group
        else: #if there is no last_node_previous_part like first group whose previous points to none
            head = previous

        #connect with next part
        last_node_of_sub_list = current


        if current is None:
            break
        previous = last_node_of_sub_list

    return head


def main ():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are : ", end = '')
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print ("Nodes of reversed LinkedList are : ", end = '')
    result.print_list()

main()