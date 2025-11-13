class Solution:
    def maxOperations(self, s: str) -> int:
        count_one = ans = 0
        i, n = 0, len(s)
        
        while i < n:
            if s[i] == '0':
                while i + 1 < n and s[i + 1] == '0':
                    i += 1
                ans += count_one
            else:
                count_one += 1
            i += 1
        
        return ans
