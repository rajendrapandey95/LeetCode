from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(nums[i] < nums[i - 1] for i in range(1, len(nums))) + (nums[0] < nums[-1]) <= 1
