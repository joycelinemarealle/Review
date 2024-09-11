class Node:
    def __init__(self, data=None, next=None ):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

#utility function to test out linked list
    def print(self):
        if self.head is None: #blank linked list
            print("Linked list is empty")
            return

        itr = self.head #if not blank temp variable
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None) #next element is none since at end
            return

        itr = self.head #if not none then not at the end . iterate until reach end
        while itr.next: #if there is next
            itr = itr.next
            #when itr.next is none then
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0 : #check condition if want to remove the head
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index -1 : #stop element before the index
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1

    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception ("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return
        #for other cases
        #initialize count
        count = 0
        itr = self.head #reference first node

        while itr:
            if count == index -1: #need to modify pointer of previous element before index
               node = Node (data,itr.next ) #create a node next is my previous next
               itr.next = node
               break

            itr = itr.next # each element through list
            count += 1 #increment count



if __name__ == '__main__':
    ll = LinkedList()
    #   ll.insert_at_begining(5)
    #   ll.insert_at_begining(89)
    #  ll.insert_at_end(79)
    ll.insert_values(["a", "b", "c", "d"])
    ll.print()
    #print('length', ll.get_length())
    # ll.remove_at(2)
    ll.insert_at(2, "e")
    ll.insert_at(0, "g")
    ll.print()