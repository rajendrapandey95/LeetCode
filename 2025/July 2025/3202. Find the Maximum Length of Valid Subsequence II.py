class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        res = 0
        for x in nums:
            x %= k
            for y in range(k):
                dp[y][x] = dp[x][y] + 1
                res = max(res, dp[y][x])
        return res
