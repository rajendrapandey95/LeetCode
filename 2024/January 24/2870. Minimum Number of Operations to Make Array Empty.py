from collections import Counter
from math import ceil
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Use Counter to count the frequency of each element in the array
        counter = Counter(nums)

        # Initialize the total number of operations
        ans = 0

        # Iterate through the Counter
        for _, c in counter.items():
            if c == 1:
                return -1
            ans += ceil(c / 3)

        return ans
