class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s2)
        dp = [0] * (m + 1)

        for c1 in s1:
            prev = 0
            for j, c2 in enumerate(s2, 1):
                cur = dp[j]
                dp[j] = prev + ord(c1) if c1 == c2 else max(dp[j], dp[j - 1])
                prev = cur

        return sum(map(ord, s1)) + sum(map(ord, s2)) - 2 * dp[m]
