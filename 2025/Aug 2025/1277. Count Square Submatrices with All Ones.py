from typing import List

class Solution:
    def countSquares(self, A: List[List[int]]) -> int:
        R, C, ans = len(A), len(A[0]), 0
        for i in range(R):
            for j in range(C):
                if A[i][j] and i and j:
                    A[i][j] += min(A[i-1][j], A[i][j-1], A[i-1][j-1])
                ans += A[i][j]
        return ans
