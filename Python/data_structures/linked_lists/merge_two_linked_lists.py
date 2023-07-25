"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together
the nodes of the first two lists.

Return the head of the merged linked list.

Example:
--------

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
"""
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
  """
  Time complexity is O(n+m) since worst case scenario we need to iterate over the entire two linked lists.
  Space complexity is O(1) as we only use a constant amount of space to store pointers.
  """
        current_node = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                current_node.next = list1
                list1, current_node = list1.next, list1
            else:
                current_node.next = list2
                list2, current_node = list2.next, list2
                
        if list1 or list2:
            current_node.next = list1 if list1 else list2
            
        return dummy.next
