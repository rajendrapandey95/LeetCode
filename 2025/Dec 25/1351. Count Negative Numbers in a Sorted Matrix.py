class Solution:
    def countNegatives(self, grid):
        i, j = len(grid) - 1, 0
        res, n = 0, len(grid[0])

        while i >= 0 and j < n:
            if grid[i][j] < 0:
                res += n - j
                i -= 1
            else:
                j += 1

        return res
