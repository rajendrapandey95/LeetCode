from typing import List
from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq = Counter(basket1) - Counter(basket2)
        freq.update(Counter(basket2) - Counter(basket1))  
        m = min(basket1 + basket2)  

        merge = []
        for k, c in freq.items():
            if c % 2:
                return -1
            merge.extend([k] * (abs(c) // 2))

        if not merge:
            return 0

        merge.sort()
        return sum(min(2 * m, x) for x in merge[: len(merge) // 2])
