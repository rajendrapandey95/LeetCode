class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        remove_set = set(nums)
        while head and head.val in remove_set:
            head = head.next
        if not head: return None
        curr = head
        while curr.next:
            if curr.next.val in remove_set:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
