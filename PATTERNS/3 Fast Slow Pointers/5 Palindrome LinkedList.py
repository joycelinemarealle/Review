#define palindrome
# 2 -> 4 ->2 same as 2-> 4 -> 2
#head == last node , second == second last so forth
#first half in forward direction == second half in backward direction
#since singly linkedlist cannot move backward
    #use fast and slow pointer to get to the middle point
    #at the middle, reverse the second half
    #compare it to first half if equal then a palindrome
    #revert the second halfback to original and bring linkedlist to original form

class Node:
    def __init__(self, value ,next = None):
        self.value = value
        self.next = next


def is_palindrome_linked_list(head):
    
    return False


def main ():
    head = Node(2)
    head.next = Node (4)
    head.next.next = Node(6)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(4)
    print ("is palindrome?" + str(is_palindrome_linked_list(head)))

main()
