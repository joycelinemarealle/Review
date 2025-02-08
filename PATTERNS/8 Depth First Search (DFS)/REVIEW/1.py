# EDGE ig root empty
# if not leaf node
# find S= s-current node. value
# recurivsely call path sum function on both left  subtree and right subtree with new number calculated from previous step

# Keep on checking if leaf node and S = to target sum
# return true

# if leaf node and S!= target sum
# return false

class TreeNode:
    def __init__(self, value, left =None, right = None):
        self.value = value
        self.left = left
        self.right = right

def has_path_sum(root, sum):
    #edge case
    if root is None:
        return False

    # it is a leaf node and S same as target sum
    if root.left is None and root.right is None and sum == root.value:
        return True
    #call recursively on both left subtree and right subtree with sum from prev step
    return has_path_sum(root.left, sum - root.value) or has_path_sum(root.right, sum- root.value)

def main ():
    root = TreeNode(12)
    root.left = TreeNode (7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(has_path_sum(root, 23))
main()



