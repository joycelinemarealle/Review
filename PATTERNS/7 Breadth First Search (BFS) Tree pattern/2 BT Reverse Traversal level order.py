from collections import deque

#push root to queue
#edge if root empty then return empty queue
# itierate through queue as long not empty
#result queues so as to append left
#store the size of queue, currentLevel array []
    #loop size of queue times
        # popleft node
        # save node value  into the currentLevel array
        #if current node has a child add node to queue

    # append left subarray currentLevel to result


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None


def traverse(root):
    #edge case
    result = deque() #easily append left the subarray. Unlinke array will have to shift all exisiting element
    if root is None:
        return result

    #push root to queue
    queue= deque()
    queue.append(root)
    #Iterate through queue as long as not empty
    while queue:
        #Store size of queue and initialize empty array for sublevel
        levelSize = len(queue)
        currentLevel = []

        #Repeat popping node from queue for levelsize times
        for _ in range(levelSize):
            currentNode = queue.popleft()

            #add node value to currentLevel subarray
            currentLevel.append(currentNode.value)

            #if node has children then push to queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        result.appendleft(currentLevel)
    return result


def main ():
    root = TreeNode(1)
    root.left =TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print("Reverse Traversal Nodee "+ str(traverse(root)))

main ()
#O(N)


