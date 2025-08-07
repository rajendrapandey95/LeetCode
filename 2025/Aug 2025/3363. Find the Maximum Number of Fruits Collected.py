from typing import List

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        ans = sum(fruits[i][i] for i in range(n)) 

        def dp_path_sum(grid: List[List[int]]) -> int:
            prev = [float("-inf")] * n
            prev[n - 1] = grid[0][n - 1]

            for i in range(1, n - 1):
                curr = [float("-inf")] * n
                for j in range(max(n - 1 - i, i + 1), n):
                    max_prev = prev[j]
                    if j - 1 >= 0:
                        max_prev = max(max_prev, prev[j - 1])
                    if j + 1 < n:
                        max_prev = max(max_prev, prev[j + 1])
                    curr[j] = max_prev + grid[i][j]
                prev = curr
            return prev[n - 1]

        ans += dp_path_sum(fruits)

        for i in range(n):
            for j in range(i):
                fruits[i][j], fruits[j][i] = fruits[j][i], fruits[i][j]

        ans += dp_path_sum(fruits)
        return ans
