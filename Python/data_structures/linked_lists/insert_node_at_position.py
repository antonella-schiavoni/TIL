# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(llist, data, position):
    new_node = SinglyLinkedListNode(data)
    if position == 0:
        new_node.next = llist
        return new_node
    
    current_node = llist
    current_node_idx = 0
    while current_node_idx +1 != position:
        current_node = current_node.next
        current_node_idx += 1
        
    aux_node = current_node.next
    current_node.next = new_node
    new_node.next = aux_node
    
    return llist
