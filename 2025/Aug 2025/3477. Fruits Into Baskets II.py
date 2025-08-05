from typing import List
import bisect

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        baskets.sort()
        count = 0

        for fruit in fruits:
            i = bisect.bisect_left(baskets, fruit) 
            if i == len(baskets):
                count += 1  
            else:
                baskets.pop(i)  
        return count
