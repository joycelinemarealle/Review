from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

def find_minimum_tree(root):
    #Edge case
    if root is None:
        return 0

    # 1 initialization
    minimum_depth = 0

    #2 Push root to queue
    queue = deque()
    queue.append(root)

    #3 Iterate through queue as long not empty to track path from root to child
    while queue:
        #4  Track count for each level +  #track number of nodes in queue to help in for loop
        minimum_depth += 1
        levelSize = len(queue)

        #Process each node in current level using for loop levelSize times
        for _ in range (levelSize):
            currentNode = queue.popleft()

            #Check if there is a leaf node
            #consider using if currentNodeleft is None which is more precise and not false(none, 0 , empty)
            if not currentNode.left and not currentNode.right:
                return minimum_depth

            #Push children of node to queue for next level
            if currentNode.left:
                 queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

def main ():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print ("Minimum depth of binary Tree "+ str(find_minimum_tree(root)))
main ()