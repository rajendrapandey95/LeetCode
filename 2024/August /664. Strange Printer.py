import itertools

class Solution:
    def strangePrinter(self, s: str) -> int:
        s = "".join(char for char, _ in itertools.groupby(s))
        n = len(s)

        dp = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                for k in range(start, end):
                    if s[k] == s[end]:
                        dp[start][end] = min(dp[start][end], dp[start][k] + dp[k + 1][end] - 1)
                    else:
                        dp[start][end] = min(dp[start][end], dp[start][k] + dp[k + 1][end])

        return dp[0][n - 1]
