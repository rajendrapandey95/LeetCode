from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == nums[i + 1] and nums[i] != 0:
                nums[i] *= 2
                nums[i + 1] = 0

        write_idx = 0 
        for i in range(n):
            if nums[i] != 0:
                nums[write_idx], nums[i] = nums[i], nums[write_idx]
                write_idx += 1

        return nums
