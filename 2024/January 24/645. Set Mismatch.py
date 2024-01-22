from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        unique_sum = sum(set(nums))
        total_sum = sum(nums)
        
        repeated_num = total_sum - unique_sum
        
        expected_sum = (n * (n + 1)) // 2
        missing_num = expected_sum - unique_sum
        
        return [repeated_num, missing_num]
