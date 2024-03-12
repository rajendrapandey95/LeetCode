# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize a hashmap to store cumulative sums and their corresponding nodes
        prefix_sum = {}
        prefix_sum[0] = dummy
        current_sum = 0
        
        # Traverse the linked list to compute cumulative sums
        while head:
            current_sum += head.val
            if current_sum in prefix_sum:
                # Remove nodes from the previous occurrence of the same sum up to the current occurrence
                prev = prefix_sum[current_sum]
                start_sum = current_sum
                while prev != head:
                    prev = prev.next
                    start_sum += prev.val
                    if prev != head:
                        del prefix_sum[start_sum]
                # Adjust the pointers to skip nodes with zero sum
                prefix_sum[current_sum].next = head.next
            else:
                prefix_sum[current_sum] = head
            head = head.next
        
        return dummy.next
