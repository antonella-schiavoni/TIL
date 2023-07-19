def reverse(llist):
    # Handle the case where the list is empty or has only one node
    if not llist or not llist.next:
        return llist
    
    current_node = llist
    new_head = None
    
    # Traverse the list and reverse the pointers
    while current_node:
        next_node = current_node.next
        current_node.next = current_node.prev
        current_node.prev = next_node
        
        # Store the new head node
        new_head = current_node
        
        # Move to the next node
        current_node = next_node
    
    return new_head
