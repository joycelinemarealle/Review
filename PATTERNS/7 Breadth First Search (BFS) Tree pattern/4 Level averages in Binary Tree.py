#Intialize variable
#edge case
#result array
#push root to queue
#iterate through queue as long as not empty
    #capture size of level
    # repeat popping nodes of current level and tracking sum levelsize times
        # capture sum fo nodes in a level
    #calculate ave sum/levelsize
    #append avg in result array
#return array

from collections import deque
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None
def traverse (root):
    #To do
    #1 Initialize empty array to hold all avegs from all level
    result = []
    #edge case
    if root is None:
        return result
    #/import queue to hold nodes and pop
    queue = deque()
    #2 Push root to queue
    queue.append(root)

    #3 Iterate through queue as long as not empty
    while queue:
        #capture levelSize to know how many times loop
        levelSize = len(queue)
        sum_level = 0
        # 4 Repeat popping nodes of current level and tracking sum levelSize times
        for _ in range(levelSize):

            #pop off the node from queue
            currentNode = queue.popleft()

            #Track cumulative sum of current level . current node.value
            sum_level += currentNode.value

           #add children of current Node
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        # 5 calculate avg of level after last node in level
        avg_level = sum_level / levelSize
        # 6 Add to avg-level result
        result.append(avg_level)
    return result

def main ():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode (4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print ("Average of all tree levels" + str(traverse(root)))

main()