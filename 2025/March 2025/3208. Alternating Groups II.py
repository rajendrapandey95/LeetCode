from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors += colors[:k-1]  
        res = l = 0
        for r in range(1, len(colors)):
            if colors[r] == colors[r-1]:
                l = r
            if r - l + 1 >= k:
                res += 1
                l += 1
        return res
