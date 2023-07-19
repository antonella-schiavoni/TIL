def reverse(llist):
	current_node = llist
	previous_node = None

	while current_node:
		# guardo el siguiente nodo para no perderlo
		next_node = current_node.next
		# actualizo el current_node.next al nodo anterior
		current_node.next = previous_node
		# reemplazo el previus node con el actual
		previous_node = current_node
		# muevo el puntero al proximo nodo
		current_node = next_node

	return previous_node
