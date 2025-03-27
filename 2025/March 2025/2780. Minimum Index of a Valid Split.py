from typing import List
from collections import defaultdict

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        first_map = defaultdict(int)  
        second_map = defaultdict(int) 
        n = len(nums)

        for num in nums:
            second_map[num] += 1

        for index in range(n):
            num = nums[index]

            second_map[num] -= 1
            first_map[num] += 1

            if (
                first_map[num] * 2 > index + 1 
                and second_map[num] * 2 > n - index - 1  
            ):
                return index 

        return -1  
