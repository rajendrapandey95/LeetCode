from math import sqrt

class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c = int(sqrt(a*a + b*b))
                if c <= n and c*c == a*a + b*b:
                    res += 1
        return res
