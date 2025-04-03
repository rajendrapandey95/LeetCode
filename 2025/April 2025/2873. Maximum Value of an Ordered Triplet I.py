from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_i = nums[0] 
        max_res = 0
        min_diff = float('-inf')  
        
        for j in range(1, n - 1):
            min_diff = max(min_diff, max_i - nums[j])
            max_res = max(max_res, min_diff * nums[j + 1])
            max_i = max(max_i, nums[j])
        
        return max_res
