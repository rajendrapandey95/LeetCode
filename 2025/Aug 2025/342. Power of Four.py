class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and n==(n&-n) and (n-1)%3==0
