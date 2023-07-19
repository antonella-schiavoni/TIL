# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def sortedInsert(llist, data):
    current_node = llist
    prev_node = None
    # create the new node
    new_node = DoublyLinkedListNode(data)
    
    while current_node and current_node.data < data:
        # move to the next elem of the list
        prev_node = current_node
        current_node = current_node.next

    new_node.next = current_node
    new_node.prev = prev_node
    
    # If inserting at beginning, update head
    if prev_node is None:
        llist = new_node
    else:
        # Else update next of previous node
        prev_node.next = new_node

    if current_node:
        current_node.prev = new_node
        
    return llist
