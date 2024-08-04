from typing import List
import heapq

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10**9 + 7
        subarray_sums = []
        
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                subarray_sums.append(sum)
    
        heapq.heapify(subarray_sums)
        range_sum = 0
        
        for _ in range(left - 1):
            heapq.heappop(subarray_sums)
        
        for _ in range(right - left + 1):
            range_sum = (range_sum + heapq.heappop(subarray_sums)) % mod
        
        return range_sum
