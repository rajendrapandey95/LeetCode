class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9+7
        r = b = 0
        for i in range(1, n+1):
            if i&(i-1)==0: b+=1
            r = (r<<b | i) % mod
        return r
