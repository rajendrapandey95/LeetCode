from functools import cache

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(x, y, d, turn, target):
            nx, ny = x + DIRS[d][0], y + DIRS[d][1]
            if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] != target:
                return 0
            res = dfs(nx, ny, d, turn, 2 - target)
            if turn:
                res = max(res, dfs(nx, ny, (d + 1) % 4, False, 2 - target))
            return res + 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for d in range(4):
                        ans = max(ans, dfs(i, j, d, True, 2) + 1)
        return ans
