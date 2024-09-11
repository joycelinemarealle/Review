from jmespath.ast import current_node


class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
        def __init__(self):
            self.head = None

        def insert_at_beginning(self, data):
            node = Node (data, self.head, None)
            self.head = node
            return

        def insert_at_end(self, data):
            if self.head is None:  # If the list is empty
                self.head = Node(data)  # The new node becomes the head
                return

            # If the list is not empty, traverse to the last node
            current_node = self.head
            while current_node.next:
                current_node = current_node.next

            # Insert the new node at the end of the list
            new_node = Node(data, None, current_node)  # Set 'prev' to current last node
            current_node.next = new_node  # Link the current last node to the new node

        def print_forward(self):
            if self.head is None:
                print("Double Linked List is empty")
                return
            #iterate across nodes
            current_node = self.head
            dlstr = ' '

            #loop through node to print data and next..
            while current_node:
                dlstr += str(current_node.data) + '-->'
                current_node = current_node.next
            print(dlstr)

        def print_backward(self):
            #check if list empty
            if self.head is None:
               print("double Linked List is empty")
               return
            #if list not empty + traverse through nodes. Start with last nodes
            last_node = self.get_last_node()
            current_node = last_node
            dlstr = ' '

            #loop through nodes + print data + prev.
            while current_node:
                dlstr += str(current_node.data) + '--->'
                current_node = current_node.prev
            print (dlstr)

        def get_last_node(self):
            #If list empty
            if self.head is None:
                print('Double Linked List is empty')
                return
            #if other nodes
            current_node = self.head

            while current_node.next:
                current_node= current_node.next
            return current_node #last node after loops end

        def insert_values(self, data_list):
            self.head = None
            for data in data_list:
                self.insert_at_end(data)

        def get_length(self):
            current_index = 0
            current_node = self.head

            while current_node:
                current_index +=1
                current_node = current_node.next
            return current_index

        def insert_at(self, index, data):
            if index <0 or index > self.get_length():
                raise Exception ("Invalid Index")

            if index == 0:
                self.insert_at_beginning(data)
                return

            current_index = 0
            current_node = self.head
            while current_node:
                if current_index == index -1:
                    node= Node (data, current_node.next, current_node)
                    if current_node.next:
                        node.next.prev = node
                    break
                current_node = current_node.next
                current_index +=1

        def  remove_at (self, index):
            if index < 0 or index > self.get_length():
                raise Exception ("Invalid Index")

            if index == 0:
                self.head = self.head.next.next
                self.head.prev = None
                return

            current_index = 0
            current_node = self.head
            while current_node:
                if current_index == index:
                    current_node.prev.next = current_node.next
                    if current_index.next:
                        current_node.next.prev = current_node.prev
                        break
                current_node = current_node.next
                current_index +=1


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0, "jackfruit")
    ll.print_forward()
    ll.insert_at(6, "dates")
    ll.print_forward()
    ll.insert_at(2, "kiwi")
    ll.print_forward()