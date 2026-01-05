from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        s = 0
        mn = float('inf')
        neg = 0

        for r in matrix:
            for v in r:
                if v < 0:
                    neg += 1
                a = abs(v)
                s += a
                mn = min(mn, a)

        return s - (2 * mn if neg % 2 else 0)
