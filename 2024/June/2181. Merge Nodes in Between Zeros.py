class Solution:
    def mergeNodes(self, head):
        cur = head.next
        nxt = cur

        while nxt:
            s = 0
            while nxt.val != 0:
                s += nxt.val
                nxt = nxt.next

            cur.val = s
            nxt = nxt.next
            cur.next = nxt
            cur = cur.next
        return head.next
