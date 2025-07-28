from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for x in nums:
            max_or |= x

        count = 0
        n = len(nums)
        for mask in range(1, 1 << n):
            or_val = 0
            for i in range(n):
                if mask & (1 << i):
                    or_val |= nums[i]
            if or_val == max_or:
                count += 1
        return count
