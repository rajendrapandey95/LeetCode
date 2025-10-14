from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        cnt = pre = ans = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cnt += 1
            else:
                pre, cnt = cnt, 1
            ans = max(ans, min(pre, cnt), cnt//2)
        return ans >= k
