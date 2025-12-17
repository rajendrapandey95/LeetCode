class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        INF = 10**18
        dp = [[0, -INF, -INF] for _ in range(k + 1)]

        for p in prices:
            for j in range(k, 0, -1):
                dp[j][0] = max(dp[j][0], dp[j][1] + p, dp[j][2] - p)
                dp[j][1] = max(dp[j][1], dp[j - 1][0] - p)
                dp[j][2] = max(dp[j][2], dp[j - 1][0] + p)

        return dp[k][0]
