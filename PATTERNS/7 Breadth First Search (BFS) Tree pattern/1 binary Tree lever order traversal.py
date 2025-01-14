from collections import deque

class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


def traverse(root):

    # Initialization empty array to store subarrays for each level
    result = []

    #edge case
    if root is None:
        return result

    # 2 Push root to queue
    queue = deque()
    queue.append(root)

    #3 Keep iterating until queue  empty
    while queue:
        #4 Each iteration first count element in queue
        levelSize = len(queue)   # store size of queue this determines iterations
        currentLevel = [] #array to store nodes per level

        #5 Remove levelSize nodes from queue and push their value to a array
        for _ in range(levelSize): #repeats block this number of times
            #pop node form queue
            currentNode = queue.popleft()

            #add node to currentLevel array
            currentLevel.append(currentNode.value)

            # 6  Insert children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

            #7 Once all nodes of current level processed then add currentLevel subarry to main array
        result.append(currentLevel)

            # 7if queue not empty repeat 3
    return result

def main ():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left=TreeNode (10)
    root.right.right = TreeNode(5)

    print("Level order traversal" + str(traverse(root)))

main()
