class Solution:
    def solve(self, i, j, grid, dp):
        if i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        dp[i][j] = 1 + min(self.solve(i, j+1, grid, dp), self.solve(i+1, j+1, grid, dp), self.solve(i+1, j, grid, dp))
        return dp[i][j]

    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
        return sum(self.solve(i, j, matrix, dp) for i in range(len(matrix)) for j in range(len(matrix[0])))
