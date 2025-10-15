from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        cnt = pre = ans = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cnt += 1
            else:
                pre, cnt = cnt, 1
            ans = max(ans, min(pre, cnt), cnt // 2)
        return ans
