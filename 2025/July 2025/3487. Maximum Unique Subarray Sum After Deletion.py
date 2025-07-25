from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        pos = {x for x in nums if x > 0}
        return max(nums) if not pos else sum(pos)
