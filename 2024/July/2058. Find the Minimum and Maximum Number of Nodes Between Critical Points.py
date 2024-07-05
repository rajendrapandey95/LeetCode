class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = [-1, -1]
        min_dist = float("inf")

        prev = head
        curr = head.next
        idx = 1
        prev_crit_idx = 0
        first_crit_idx = 0

        while curr.next is not None:
            if (curr.val < prev.val and curr.val < curr.next.val) or (curr.val > prev.val and curr.val > curr.next.val):
                if prev_crit_idx == 0:
                    prev_crit_idx = idx
                    first_crit_idx = idx
                else:
                    min_dist = min(min_dist, idx - prev_crit_idx)
                    prev_crit_idx = idx

            idx += 1
            prev = curr
            curr = curr.next

        if min_dist != float("inf"):
            max_dist = prev_crit_idx - first_crit_idx
            res = [min_dist, max_dist]

        return res
