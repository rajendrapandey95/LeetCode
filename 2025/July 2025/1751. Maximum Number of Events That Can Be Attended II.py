from bisect import bisect_right

class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        events.sort()
        n, starts = len(events), [e[0] for e in events]
        dp = [[-1] * n for _ in range(k + 1)]

        def dfs(i: int, c: int) -> int:
            if c == 0 or i == n: return 0
            if dp[c][i] != -1: return dp[c][i]
            j = bisect_right(starts, events[i][1])
            dp[c][i] = max(dfs(i + 1, c), events[i][2] + dfs(j, c - 1))
            return dp[c][i]

        return dfs(0, k)
