class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def _calculate_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        current = head
        while current and current.next:
            gcd_value = _calculate_gcd(current.val, current.next.val)
            gcd_node = ListNode(gcd_value)

            gcd_node.next = current.next
            current.next = gcd_node

            current = gcd_node.next

        return head
