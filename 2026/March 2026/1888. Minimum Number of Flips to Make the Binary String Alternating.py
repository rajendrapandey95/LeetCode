class Solution:
    def minFlips(self, s: str) -> int:
        s = s + s
        n = len(s)
        alt1 = alt2 = res = n
        c1 = c2 = 0
        
        for i, ch in enumerate(s):
            if ch != "01"[i & 1]: c1 += 1
            if ch != "10"[i & 1]: c2 += 1
            
            if i >= n//2:
                res = min(res, c1, c2)
                
                if s[i-n//2] != "01"[(i-n//2) & 1]: c1 -= 1
                if s[i-n//2] != "10"[(i-n//2) & 1]: c2 -= 1
        
        return res
