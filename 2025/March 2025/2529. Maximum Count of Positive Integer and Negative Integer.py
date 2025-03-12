class Solution:
    def maximumCount(self, nums):
        pos = sum(1 for n in nums if n > 0)
        neg = sum(1 for n in nums if n < 0)
        return max(pos, neg)
