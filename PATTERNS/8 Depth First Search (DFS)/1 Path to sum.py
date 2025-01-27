#start DFS at root

# if not leaf node
 # Find new sum s=s-current node.value
 # recursive calls on both left and right child
#Keep on checking each node if leaf node and sum = node value then return true
#if current node a leaf but sum != node value then return false

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def has_path(root,sum):
    #edge case
    #if root is empty
    if root is None:
        return False

    #Check if lead node and sum = node value of lead node
    if root.value == sum and root.left is None and root.right is None:
        return True

    #If not lead node then call recursively function on both left and right child
    #recursive call to traverse left and right sub-tree
    #return true if any of recursive call returns true
    return has_path(root.left, sum - root.value) or has_path((root.right) , sum - root.value)

def main ():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print (has_path(root,23))
main ()