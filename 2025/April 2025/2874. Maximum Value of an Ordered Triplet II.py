from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0  

        leftMax = [0] * n
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], nums[i - 1])

        rightMax = [0] * n
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], nums[i + 1])

        res = 0
        for j in range(1, n - 1):
            res = max(res, (leftMax[j] - nums[j]) * rightMax[j])

        return res
