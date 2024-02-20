from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        expected_sum = n * (n + 1) // 2  # Correcting the calculation
        
        actual_sum = sum(nums)
        
        missing_number = expected_sum - actual_sum
        
        return missing_number
