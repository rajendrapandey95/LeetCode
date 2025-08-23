class Solution:
    def minimumSum2(self, grid, u, d, l, r):
        min_i, max_i, min_j, max_j = len(grid), -1, len(grid[0]), -1
        for i in range(u, d + 1):
            for j in range(l, r + 1):
                if grid[i][j]:
                    min_i, max_i = min(min_i, i), max(max_i, i)
                    min_j, max_j = min(min_j, j), max(max_j, j)
        return (max_i - min_i + 1) * (max_j - min_j + 1) if min_i <= max_i else 10**9

    def rotate(self, g):
        return [list(row) for row in zip(*g[::-1])]

    def solve(self, g):
        n, m, res = len(g), len(g[0]), len(g) * len(g[0])
        for i in range(n - 1):
            for j in range(m - 1):
                res = min(res,
                          self.minimumSum2(g, 0, i, 0, m - 1) +
                          self.minimumSum2(g, i + 1, n - 1, 0, j) +
                          self.minimumSum2(g, i + 1, n - 1, j + 1, m - 1),
                          self.minimumSum2(g, 0, i, 0, j) +
                          self.minimumSum2(g, 0, i, j + 1, m - 1) +
                          self.minimumSum2(g, i + 1, n - 1, 0, m - 1))
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                res = min(res,
                          self.minimumSum2(g, 0, i, 0, m - 1) +
                          self.minimumSum2(g, i + 1, j, 0, m - 1) +
                          self.minimumSum2(g, j + 1, n - 1, 0, m - 1))
        return res

    def minimumSum(self, grid):
        return min(self.solve(grid), self.solve(self.rotate(grid)))
