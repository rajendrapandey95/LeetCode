from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        last = [-1] * 32 

        for i in range(n - 1, -1, -1):
            last_set = i
            for bit in range(32):
                if nums[i] & (1 << bit):
                    last[bit] = i
                elif last[bit] != -1:
                    last_set = max(last_set, last[bit])
            ans[i] = last_set - i + 1
        return ans
