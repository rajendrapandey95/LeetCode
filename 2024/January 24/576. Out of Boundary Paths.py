class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  

        dp = [[[0] * (maxMove + 1) for _ in range(n)] for _ in range(m)]

        dp[startRow][startColumn][0] = 1

        result = 0

        for move in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    for d in directions:
                        ni, nj = i + d[0], j + d[1]

                        if 0 <= ni < m and 0 <= nj < n:
                            dp[i][j][move] = (dp[i][j][move] + dp[ni][nj][move - 1]) % MOD
                        else:
                            
                            result = (result + dp[i][j][move - 1]) % MOD

        return result
