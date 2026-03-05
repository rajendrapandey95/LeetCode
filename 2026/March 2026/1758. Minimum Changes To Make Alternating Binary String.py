class Solution:
    def minOperations(self, s: str) -> int:
        a = b = 0
        
        for i, c in enumerate(s):
            if c != "01"[i & 1]: a += 1
            if c != "10"[i & 1]: b += 1
        
        return min(a, b)
