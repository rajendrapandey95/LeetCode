from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        prefix = [0]
        indices = []
        for pos, amount in fruits:
            indices.append(pos)
            prefix.append(prefix[-1] + amount)

        def collect(left: int, right: int) -> int:
            return prefix[bisect_right(indices, right)] - prefix[bisect_left(indices, left)]

        ans = 0
        for x in range(k // 2 + 1):
            ans = max(ans, collect(startPos - x, startPos + (k - 2 * x)))
            ans = max(ans, collect(startPos - (k - 2 * x), startPos + x))
        return ans
