class Solution:
    def maxFreeTime(self, T: int, s: list[int], e: list[int]) -> int:
        n, q, t1, t2 = len(s), [0]*len(s), 0, 0
        for i in range(n):
            if e[i] - s[i] <= t1: q[i] = 1
            t1 = max(t1, s[i] - (0 if i == 0 else e[i - 1]))
            j = n - i - 1
            if e[j] - s[j] <= t2: q[j] = 1
            t2 = max(t2, (T if i == 0 else s[j + 1]) - e[j])
        res = 0
        for i in range(n):
            l = 0 if i == 0 else e[i - 1]
            r = T if i == n - 1 else s[i + 1]
            res = max(res, r - l if q[i] else r - l - (e[i] - s[i]))
        return res
