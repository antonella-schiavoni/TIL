# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteNode(llist, position):
    if llist is None or position == 0:
        llist = llist.next
        return llist
    
    current_node = llist
    current_node_idx = 0
    while current_node_idx +1 != position:
        current_node = current_node.next
        current_node_idx += 1
        
    current_node.next = current_node.next.next
    return llist
