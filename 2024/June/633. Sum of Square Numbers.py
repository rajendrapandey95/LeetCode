class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a * a <= c:
            b = (c - a * a) ** 0.5
            if b == int(b):
                return True
            a += 1
        return False
