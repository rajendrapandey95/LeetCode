class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        g, m, q = 0, {}, {}
        for x in sorted(nums):
            if g not in q or abs(x - q[g][-1]) > limit: g += 1
            m[x] = g
            q.setdefault(g, deque()).append(x)
        return [q[m[x]].popleft() for x in nums]
