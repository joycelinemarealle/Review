from collections import deque
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left, self.right = None, None


def level_order_successor(root,key):
    #Edge case
     if root is None:
         return None
    #Push root to queue
     queue = deque ()
     queue.append(root)

     #Process each node of every node Iterate through
     while queue:
         # popleft each node in queue
        currentNode = queue.popleft()

        # if current node has a  child node add to queue
        if currentNode.left:
             queue.append(currentNode.left)

        if currentNode.right:
             queue.append(currentNode.right)

         #if node == key break loop
        if currentNode.value == key:
             break

     #return the first node
     return queue[0].value if queue else None


def main ():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(level_order_successor(root,2))

main()