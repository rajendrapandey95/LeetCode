import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        num_operations = 0

        while nums[0] < k:
            first = heapq.heappop(nums)
            second = heapq.heappop(nums)
            new_value = first * 2 + second 
            heapq.heappush(nums, new_value)
            num_operations += 1

        return num_operations
