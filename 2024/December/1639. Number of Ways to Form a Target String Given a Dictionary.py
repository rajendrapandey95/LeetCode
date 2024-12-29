class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        dp = [[-1] * len(target) for _ in range(len(words[0]))]
        char_freq = [[0] * 26 for _ in range(len(words[0]))]

        for word in words:
            for i, char in enumerate(word):
                char_freq[i][ord(char) - 97] += 1

        def dfs(w_idx: int, t_idx: int) -> int:
            if t_idx == len(target):
                return 1
            if w_idx == len(words[0]) or len(words[0]) - w_idx < len(target) - t_idx:
                return 0
            if dp[w_idx][t_idx] != -1:
                return dp[w_idx][t_idx]

            dp[w_idx][t_idx] = dfs(w_idx + 1, t_idx) + char_freq[w_idx][ord(target[t_idx]) - 97] * dfs(w_idx + 1, t_idx + 1)
            dp[w_idx][t_idx] %= 1000000007
            return dp[w_idx][t_idx]

        return dfs(0, 0)
