class Solution:
    def maxFreeTime(self, t: int, k: int, s: list[int], e: list[int]) -> int:
        n, res = len(s), 0
        total = [0] * (n + 1)
        for i in range(n):
            total[i + 1] = total[i] + e[i] - s[i]
        for i in range(k - 1, n):
            r = t if i == n - 1 else s[i + 1]
            l = 0 if i == k - 1 else e[i - k]
            res = max(res, r - l - (total[i + 1] - total[i - k + 1]))
        return res
