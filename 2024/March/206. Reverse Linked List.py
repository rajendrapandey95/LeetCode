class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        curr_node = head
        
        while curr_node:
            next_node = curr_node.next  # Store reference to next node
            curr_node.next = prev_node  # Reverse pointer direction
            
            # Move to the next pair of nodes
            prev_node = curr_node
            curr_node = next_node
        
        # At the end, prev_node will be the new head of the reversed list
        return prev_node
