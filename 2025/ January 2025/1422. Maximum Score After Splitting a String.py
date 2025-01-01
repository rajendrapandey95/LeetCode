class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(1, len(s)):
            res = max(res, s[:i].count("0") + s[i:].count("1"))
        return res
