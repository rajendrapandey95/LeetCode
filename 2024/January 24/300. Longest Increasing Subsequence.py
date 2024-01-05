from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        tails = [0] * len(nums)
        size = 0  

        for num in nums:
            left, right = 0, size
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            if left == size:
                tails[size] = num
                size += 1
            else:
                tails[left] = num

        return size
