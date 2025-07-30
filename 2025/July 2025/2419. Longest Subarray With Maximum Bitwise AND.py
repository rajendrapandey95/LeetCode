from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        ans = streak = 0
        for num in nums:
            if num == max_val:
                streak += 1
                ans = max(ans, streak)
            else:
                streak = 0
        return ans
