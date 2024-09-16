
#Hash functions
def get_hash(key):
    sum = 0
    for char in key: #going through all characteristics and finding as key value of each character
        sum+=ord(char)
    return sum % 100 #return a remainder after sum divided by 100 so remainder between 0-99
print (get_hash("march 6"))


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

#mechanism of creating keys
    def get_hash(self, key):
        sum = 0
        for char in key:
            sum +=ord(char)
        return sum % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

#create  object
if __name__ == '__main__':
    t = HashTable()
    #(print(t.get_hash('march 6'))
    t['march 6'] = 130
    t['march 9'] = 500
    t['augusut 1'] = 200
    print(t.arr)
    print(t['march 6'])
    t.__delitem__('march 6')
    print(t.arr)