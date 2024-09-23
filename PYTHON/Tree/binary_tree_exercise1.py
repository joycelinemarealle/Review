from binary_search import build_tree


class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # if val == self.data
        if self.data == data:
            return #end function since cant have duplicate

        #if data < self.data
        if data < self.data: #if node is not empty then compare data and self.data
            if self.left is not None:
                self.left.add_child(data)
            else: #empty node then create a node with val as data
                self.left = BinarySearchTreeNode(data)

        #if data  > self.data
        if data > self.data:
            if self.right is not None:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self,data):
        #if  data == self.data
             if data == self.data:
                 return True #found the data

             #if data < self.data , might be on left
             if data < self.data:
                 if self.left is not None:
                     return self.left.search(data)
                 else:
                     return False
             #if data > self.data , might be right
             if data > self.data:
                 if self.right is not None:
                     return self.right.search(data)
                 else:
                     return False

    def in_order_traversal(self):
        #empty array to store values
        elements = []

        #left ->node -> right

        #visit left tree
        if self.left is not None:
           elements += self.left.in_order_traversal

        #visit base node
        elements.append(self.data)

        #visit right tree
        if self.right is not None:
            elements+= self.right.in_order_traversal

        return elements

    def post_order_traversal(self):
        # left -> right -> node
        elements = []

        #visit left tree
        if self.left is not None:
            elements+=self.left.post_order_traversal()

        #visit right tree
        if self.right is not None:
            elements += self.right.post_order_traversal()

        #visit node
        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        # right -> left -> node
        elements = []


        #visit node
        elements.append(self.data)

        # visit left tree
        if self.left is not None:
            elements += self.left.post_order_traversal()

        # visit right tree
        if self.right is not None:
            elements += self.right.post_order_traversal()

        return elements

    def sum(self):
        sum = 0

        #start with nodes own data
        sum += self.data

        #Recursvively add the left subtree if exists
        if self.left is not None:
            sum += self.left.sum()

        #recursively add sum of right subtree if exists
        if self.right is not None:
            sum += self.right.sum()

        return sum

    def find_min(self):
        # The min on the left side. The most left = min
        # Base case: if there's no left child, the current node is the minimum
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()

    def find_max(self):
        #The max on right side. The most right = max
        #Base case: if there is no right child, the current node is the max
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()




def build_helper(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17,14,1,20,9,23,18,24]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(20))

 #check data at node set as minimum
        # minimum = self.data
        #
        # #check if left node less than minimum then set as new min.  call find minimum recursively
        # if self.left is not None:
        #     #if left node less or not call recursively
        #     if self.left.data < minimum:
        #         minimum = self.left.data
        #     else:
        #         return self.left.find_min()
        #
        # else:
        #     return
        #
        # if self.right is not None:
        #     if self.right.data < minimum:
        #         minimum = self.right.data
        #     else:
        #         self.right.find_min()
        # else:
        #     return
        #
        # return minimum
