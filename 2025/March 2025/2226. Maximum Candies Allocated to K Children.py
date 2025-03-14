from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 0, max(candies)

        while left < right:
            mid = (left + right + 1) // 2
            if sum(c // mid for c in candies) >= k:
                left = mid
            else:
                right = mid - 1

        return left
