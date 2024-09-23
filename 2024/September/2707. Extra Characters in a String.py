class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n, d_set, dp = len(s), set(dictionary), [0] * (len(s) + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]
            for j in range(i, n):
                if s[i:j+1] in d_set:
                    dp[i] = min(dp[i], dp[j + 1])

        return dp[0]
