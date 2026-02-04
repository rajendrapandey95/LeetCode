class Solution:
    def numMagicSquaresInside(self, grid):
        m, n = len(grid), len(grid[0])
        ans = 0

        for r in range(m - 2):
            for c in range(n - 2):
                if grid[r + 1][c + 1] != 5:
                    continue

                nums = [grid[r+i][c+j] for i in range(3) for j in range(3)]
                if set(nums) != set(range(1, 10)):
                    continue

                s = sum(grid[r][c:c+3])
                if (
                    sum(grid[r+1][c:c+3]) == s and
                    sum(grid[r+2][c:c+3]) == s and
                    grid[r][c] + grid[r+1][c] + grid[r+2][c] == s and
                    grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == s and
                    grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == s and
                    grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == s and
                    grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == s
                ):
                    ans += 1

        return ans
