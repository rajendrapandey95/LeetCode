from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        max_money = [0] * len(nums)

        max_money[0] = nums[0]
        max_money[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            max_money[i] = max(max_money[i-1], max_money[i-2] + nums[i])

        return max_money[-1]
