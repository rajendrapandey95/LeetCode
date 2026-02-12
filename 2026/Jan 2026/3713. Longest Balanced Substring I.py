class Solution:
    def longestBalanced(self, s: str) -> int:
        from collections import defaultdict
        
        n, ans = len(s), 0
        
        for i in range(n):
            cnt = defaultdict(int)
            for j in range(i, n):
                cnt[s[j]] += 1
                vals = cnt.values()
                if min(vals) == max(vals):
                    ans = max(ans, j - i + 1)
        
        return ans
