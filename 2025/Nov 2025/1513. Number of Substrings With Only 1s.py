class Solution:
    def numSub(self, s: str) -> int:
        ans = cnt = 0
        MOD = 10**9 + 7
        
        for ch in s:
            if ch == '1':
                cnt += 1
            else:
                ans += cnt * (cnt + 1) // 2
                cnt = 0
        
        return (ans + cnt * (cnt + 1) // 2) % MOD
