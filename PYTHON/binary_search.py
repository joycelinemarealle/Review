
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
                return self.left.search(val) #recursively check if have left
            else:
                return False

        # might be on right tree
        if val > self.data:
            if self.right:
                return self.right.search(val) #recursively check if have right
            else:
                return False

    def find_min(self):
        # The min on the left side. The most left = min
        # Base case: if there's no left child, the current node is the minimum
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()

    def find_max(self):
        # The max on right side. The most right = max
        # Base case: if there is no right child, the current node is the max
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()

    def delete(self,val):
        #left subtree of current node
        if val < self.data:
            if self.left is not None:
                #assign new subtree
                self.left = self.left.delete(val) #call recursively until val == self.data of node
            else:
                return None #default behavior
        #right subtree of current node
        elif val > self.data:
            if self.right is not None:
                #asign new subtree
               self.right =  self.right.delete(val) #call delete recusrively
            else:
                return None #empty node
        # if val == self.data then delete
        #leaf nodes cases
        else:
            # leaf nodes of right and left
            if self.left is None and self.right is None:
                return None
            if self.left is None: #if no left child
                return self.right #return one child back to parent node so current node gets deleted

            if self.right is None: #if no right child
                return self.left

            #find min in right tree
            min_val = self.right.find_min()

            #replace current node with min
            self.data = min_val

            #delete duplicate min val now at right of current node
            self.right = self.right.delete(min_val)

            return self


    #helper method
def build_tree(elements):
        root = BinarySearchTreeNode(elements[0])

        for i in range (1,len(elements)):
            root.add_child(elements[i])

        return root

if __name__ == '__main__':
    numbers = [17,14,1,20,9,23,18,34]
    number_tree = build_tree(numbers)
    print(number_tree.in_order_traversal())
    print(number_tree.search(20))
    number_tree.delete(20)
    print("After deleting 20",number_tree.in_order_traversal())


