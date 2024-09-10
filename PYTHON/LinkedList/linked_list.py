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
        while itr.next: #if there is nexr
            itr = itr.next

            #when itr.next is none then
        itr .next = Node(data, None)

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
            raise Exception("Invali index")
        if index == 0 :
            self.head = self.head.next
            return

if __name__ == '__main__':
    ll = LinkedList()
 #   ll.insert_at_begining(5)
 #   ll.insert_at_begining(89)
  #  ll.insert_at_end(79)
    ll.insert_values(["a", "b", "c"])
    ll.print()
    #print('length', ll.get_length())
    ll.remove