class Solution:
    def reverse(self, n):
        sign = -1 if n < 0 else 1
        n = abs(n)
        r = 0
        while n:
            r = r*10 + n%10
            n//=10
        return sign*r

    def mirrorDistance(self, n):
        return abs(n - self.reverse(n))
