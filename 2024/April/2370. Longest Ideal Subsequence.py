class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[0] * 26 for _ in range(n)]

        for i in range(n):
            for j in range(26):
                dp[i][j] = max(dp[i][j], (dp[i - 1][j] if i > 0 else 0))

                if i == 0 or abs(ord(s[i]) - ord(s[i - 1])) <= k:
                    dp[i][ord(s[i]) - ord('a')] = max(dp[i][ord(s[i]) - ord('a')], dp[i - 1][j] + 1)

        return max(max(row) for row in dp)
