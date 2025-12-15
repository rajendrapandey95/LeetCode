class Solution:
    def getDescentPeriods(self, p: List[int]) -> int:
        a = c = 1
        for i in range(1, len(p)):
            c = c + 1 if p[i] == p[i - 1] - 1 else 1
            a += c
        return a
