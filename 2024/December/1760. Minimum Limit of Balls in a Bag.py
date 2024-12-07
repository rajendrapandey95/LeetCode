import math
from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)

        while left < right:
            middle = (left + right) // 2
            if sum((num - 1) // middle for num in nums) <= maxOperations:
                right = middle
            else:
                left = middle + 1

        return left
