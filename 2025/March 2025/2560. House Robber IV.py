from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = 1, max(nums)

        while left < right:
            mid = (left + right) // 2
            count, i = 0, 0
            
            while i < len(nums):
                if nums[i] <= mid:
                    count += 1
                    i += 1 
                i += 1  

            if count >= k:
                right = mid
            else:
                left = mid + 1

        return left
