
class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        #if data exist do not add since binary does not accept duplicates
        if data == self.data:
            return
        # add data to left subtree
        if data < self.data:
            if self.left: #if exists add child recursively
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        # add data to right subtree if data > self.data
        else:
            if self.right :
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def in_order_traversal(self):
        #vist left tree-> base node -> right tree. Node in middle
        elements = []
        #vist left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit base node
        elements.append(self.data)
        # vist right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search (self,val):
        if self.data == val :
            return True
        # might be on left tree
        if val < self.data:
            if self.left:
                self.left.search(val) #recursively check if have left
            else:
                return False

        # might be on right tree
        if val > self.data:
            if self.right:
                self.right.search(val) #recursively check if have right
            else:
                return False

    #helper method
def build_tree(elements):
        root = BinarySearchTreeNode(elements[0])

        for i in range (1,len(elements)):
            root.add_child(elements[i])

        return root

if __name__ == '__main__':
    numbers = [17,14,1,20,9,23,18,24]
    number_tree = build_tree(numbers)
    print(number_tree.in_order_traversal())
    print(number_tree.search(20))


