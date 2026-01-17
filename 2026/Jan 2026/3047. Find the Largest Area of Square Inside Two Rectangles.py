from typing import List
from itertools import combinations

class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        max_size = 0

        for (bl_i, tr_i), (bl_j, tr_j) in combinations(zip(bottomLeft, topRight), 2):
            w = min(tr_i[0], tr_j[0]) - max(bl_i[0], bl_j[0])
            h = min(tr_i[1], tr_j[1]) - max(bl_i[1], bl_j[1])

            if w > 0 and h > 0:
                max_size = max(max_size, min(w, h))

        return max_size * max_size
