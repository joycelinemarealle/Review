#Implement hash table where collisions are handled using linear probing.
# We learnt about linear probing in the video tutorial.
# Take the hash table implementation that uses chaining and modify methods to use linear probing.
# Keep MAX size of arr in hashtable as 10.
from altair import value


class Hash_Table:
    def __init__(self):
        self.Max = 10
        self.array = [None for i in range(self.Max)]

    def get_hash(self, key):
        #march 6, sum askii
        sum =0
        for char in key:
            sum += ord(char)
            return sum % self.Max

    def __getitem__(self, key):
        #get hash value
        hash_val = self.get_hash(key)
        return self.array[hash_val]

    def __setitem__(self, key, value):
        #get hash value using key
        hash_val = self.get_hash(key)

        #Find next available slot
        start_hash = hash_val
        #if slot occupied
        while self.array[hash_val] is not None:
            hash_val = (hash_val +1) % self.Max #circular array prevent out or bound
        #after loop and back to original
        if start_hash == hash_val:
            raise Exception ("HashTable is full")

        #if empty slot found then add value
        if self.array[hash_val] is None:
            self.array[hash_val] = value


if __name__ == '__main__':
    t = Hash_Table()
    t.__setitem__('march 6', 120)
    t.__setitem__('march 6', 78)
    t.__setitem__('march 8', 67)
    t.__setitem__('march 9', 4)
    t.__setitem__('march 17', 459)
    print(t.array)