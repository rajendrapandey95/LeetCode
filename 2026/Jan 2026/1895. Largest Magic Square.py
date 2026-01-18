class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        rs = [[0]*(n+1) for _ in range(m)]
        cs = [[0]*n for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                rs[i][j+1] = rs[i][j] + grid[i][j]
                cs[i+1][j] = cs[i][j] + grid[i][j]

        for k in range(min(m, n), 1, -1):
            for i in range(m-k+1):
                for j in range(n-k+1):
                    s = rs[i][j+k] - rs[i][j]

                    if any(rs[i+r][j+k] - rs[i+r][j] != s for r in range(k)):
                        continue

                    if any(cs[i+k][j+c] - cs[i][j+c] != s for c in range(k)):
                        continue

                    if sum(grid[i+d][j+d] for d in range(k)) != s:
                        continue
                    if sum(grid[i+d][j+k-1-d] for d in range(k)) != s:
                        continue

                    return k
        return 1
