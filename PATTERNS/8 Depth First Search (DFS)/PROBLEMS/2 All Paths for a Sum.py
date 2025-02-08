
class TreeNode:
    def __init__(self, value , left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def find_paths(root,sum):
    # 1 Empty list to hold all paths in main function
    allPaths = []
    #call helper function to start recursion
    find_paths_recursive(root, sum, [], allPaths)
    return allPaths

  #2 Helper function that does recursion
def find_paths_recursive(currentNode,sum, currentPath, allPaths):
    #2 Edge case of root
    if currentNode is None:
        return

    #3 Add current node into current Path
    currentPath.append(currentNode.value)

    #4 Check if it is a leaf node and if its value == sum , save current path into the all Paths list
    if currentNode.value == sum and currentNode.left is None and currentNode.right is None:
        allPaths.append(currentPath)

    else: #if not leaf node
        #traverse through left sub-tree and update the sum (sum -currenotNode.value)
        find_paths_recursive(currentNode.left, sum - currentNode.value,currentPath, allPaths)

        #traverse through right sub-tree
        find_paths_recursive(currentNode.right, sum -currentNode.value,currentPath, allPaths)
    #this runs when the if and else conditions not met meaning leaf node with no sum matching target
    #never gets here if recursion is happening traversing left/right subtree
    # when reached leaf node, remove current node from path to backtrack
    #remove the current node when going up recursive call stack
    del currentPath[-1]
def main():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode (5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(7)
    sum = 23
    print ("Tree paths with sum "+ str (sum) +  ": "+ str(find_paths(root,sum)))

main()

#back remove 4 then at 7 if 5 removed then 7 has no node. leaf node backtack to 1