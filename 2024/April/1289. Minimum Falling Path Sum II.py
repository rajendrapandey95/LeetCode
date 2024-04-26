from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            dp[0][j] = grid[0][j]
        
        for i in range(1, n):
            for j in range(n):
                min_prev = float('inf')
                for k in range(n):
                    if k != j:
                        min_prev = min(min_prev, dp[i-1][k])
                dp[i][j] = grid[i][j] + min_prev
        
        min_sum = min(dp[n-1])
        return min_sum
