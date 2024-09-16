
#Hash functions
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)] #empty array since storing key value pair

#mechanism of creating keys
    def get_hash(self, key):
        sum = 0
        for char in key:
            sum +=ord(char)
        return sum % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element [1]

    # now have linkedlist in location
    # check if key there
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        #check if key already exist before appending linked list
        #loop through all key value pairs in the linkedlist at element
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element) ==2 and element[0] == key: #it element has 2 two items key & pai
                self.arr[h][index] = (key,val) #first key-pai in linkedlist
                found = True
                break
        if not found:
            self.arr[h].append((key,val))

    # locate index,
    # then iterate through all in element
    #check if key equal to element []
    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate (self.arr[h]) :
            if element [0] == key:
                del self.arr[h][index]

#create  object
if __name__ == '__main__':
    t = HashTable()
    t.__setitem__('march 6', 120)
    t.__setitem__('march 6', 78)
    t.__setitem__('march 8', 67)
    t.__setitem__('march 9', 4)
    t.__setitem__('march 17', 459)
    print(t.get_hash('march 17'))
    print(t.__getitem__('march 6'))
    print(t.arr)
   # t.__delitem__('march 6')
   #print(t.arr)