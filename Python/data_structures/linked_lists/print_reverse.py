# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reversePrint(llist):
    # Write your code here
     # Base case: if head is None (end of list reached), return without doing anything
    if llist is None:
        return

    # Recursive call with the next node
    reversePrint(llist.next)

    # After the recursive call, print the data of the current node
    print(llist.data)
