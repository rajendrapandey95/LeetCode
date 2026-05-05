class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head

        n, tail = 1, head
        while tail.next:
            tail = tail.next
            n += 1

        k %= n
        if k == 0:
            return head

        tail.next = head

        cur = head
        for _ in range(n - k - 1):
            cur = cur.next

        new_head = cur.next
        cur.next = None

        return new_head
