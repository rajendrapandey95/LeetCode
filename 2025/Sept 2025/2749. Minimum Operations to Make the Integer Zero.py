class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(61):
            x=num1-k*num2
            if x>=k and bin(x).count("1")<=k: return k
        return -1
