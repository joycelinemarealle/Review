class Node:
    def __init__(self, data=None, next=None ):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

#utility function to test out linked list
    def print(self):
        if self.head is None: #blank linked list
            print("Linked list is empty")
            return

        current_node = self.head #if not blank temp variable
        llstr = ''

        while current_node:
            llstr += str(current_node.data) + '-->'
            current_node = current_node.next
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None) #next element is none since at end
            return

        current_node = self.head #if not none then not at the end . iterate until reach end
        while current_node.next: #if there is next
            current_node = current_node.next
            #when current_node.next is none then
        current_node.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        current_index = 0
        current_node = self.head
        while current_node:
            current_index+=1
            current_node = current_node.next
        return current_index

    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0 : #check condition if want to remove the head
            self.head = self.head.next
            return
        current_index = 0
        current_node = self.head
        while current_node:
            if current_index == index -1 : #stop element before the index
                current_node.next = current_node.next.next
                break
            current_node = current_node.next
            current_index +=1

    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception ("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return
        #for other cases
        #initialize current_index
        current_index = 0
        current_node = self.head #reference first node

        while current_node:
            if current_index == index -1: #need to modify pointer of previous element before index
               node = Node (data,current_node.next ) #create a node next is my previous next
               current_node.next = node
               break

            current_node = current_node.next # each element through list
            current_index += 1 #increment current_index

    def insert_after_value(self, data_after, data_to_insert):

        #Condition #1.py if linkedlist is empty
        if self.head is None:
            return

        #Condition #2  first node == data_after
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)

        #Other conditions
        current_node = self.head
        while current_node:
            if current_node.data == data_after:
                node = Node (data_to_insert, current_node.next)  #create node
                current_node.next = node #then insert data after data_after node
                break

            current_node = current_node.next  # itireate through nodes

    def remove_by_value(self, data):

        #Condition #1.py if linkedlist empty
        if self.head is None:  #if ist node empty
            return
        #Condition #2 if data == self.head.data
        if self.head.data == data:
            self.head = self.head.next #removed 1st node now 2nd node is head
            return

        #Removing nodes that is not head
        current_node = self.head

        while current_node:
            if current_node.next.data == data: #
                current_node.next = current_node.next.next
                break
            current_node = current_node.next #itireate through nodes






if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.insert_after_value("mango", "apple") #insert apple after mango
    ll.print()
    ll.remove_by_value("orange") #remove orange from list
    ll.print()
    ll.remove_by_value("mango")
    ll.print()
    ll.remove_by_value("banana")
    ll.print()


