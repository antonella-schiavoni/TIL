# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    if head.next:
        print(head.data)
        printLinkedList(head.next)
    else:
        print(head.data)
