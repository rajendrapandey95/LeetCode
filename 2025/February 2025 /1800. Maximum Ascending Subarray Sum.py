from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = cur_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = nums[i] if nums[i] <= nums[i - 1] else cur_sum + nums[i]
            max_sum = max(max_sum, cur_sum)
        return max_sum
