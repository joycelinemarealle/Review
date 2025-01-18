from collections import deque
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left , self.right = None, None

def traverse(root):
    result = []
    #edge case
    if root is None:
        return result
    #push root in queue
    queue = deque()
    queue.append(root)

    #condition of direction of inserting nodes in currentLevel
    leftToRight = True
    #Iterate through queue
    while queue:
        #store size of queue to know amount of iteration
        levelSize = len(queue)
        currentLevel = deque() #easier to append left without moving elements than array list

        for _ in range(levelSize):
            # pop node form queue
            currentNode = queue.popleft()
             # and add value to
            if leftToRight:
                #add toward end of queue
               currentLevel.append(currentNode.value)

            else: #if boolean flipped
                currentLevel.appendleft(currentNode.value)

            #add children of node to queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        #add currentlevel queue to the big result
        result.append(list(currentLevel)) #convert deque to list before adding to main result

        # Reverse traversal direction flip condition for next current level appended zizzag
        leftToRight = not leftToRight
    #return the result list
    return result


def main ():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print ("Zizag level order traveral" + str(traverse(root)))

main ()