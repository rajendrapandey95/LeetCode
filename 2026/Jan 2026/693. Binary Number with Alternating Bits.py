class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = bin(n)[2:]
        return all(s[i] != s[i+1] for i in range(len(s)-1))
