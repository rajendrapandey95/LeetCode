class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        
        pre = [-1] * (n + 1)
        for i in range(n):
            if s[i] == '0':
                pre[i + 1] = i
            else:
                pre[i + 1] = pre[i]
        
        ans = 0
        
        for i in range(1, n + 1):
            cnt0 = 0
            j = i

            while j > 0:
                if s[j - 1] == '0':
                    cnt0 += 1
                
                if cnt0 * cnt0 > n:
                    break

                cnt1 = (i - j + 1) - cnt0
                
                if cnt1 >= cnt0 * cnt0:
                    ans += 1

                j = pre[j - 1] + 1 if pre[j - 1] != -1 else 0
        
        return ans
