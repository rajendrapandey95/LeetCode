from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.lower_bound(nums, upper + 1) - self.lower_bound(nums, lower)

    def lower_bound(self, nums: List[int], value: int) -> int:
        left, right, result = 0, len(nums) - 1, 0
        while left < right:
            sum_val = nums[left] + nums[right]
            if sum_val < value:
                result += right - left
                left += 1
            else:
                right -= 1
        return result
