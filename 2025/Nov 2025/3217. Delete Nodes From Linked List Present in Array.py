class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        remove = set(nums)

        while head and head.val in remove:
            head = head.next

        cur = head
        while cur and cur.next:
            if cur.next.val in remove:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
