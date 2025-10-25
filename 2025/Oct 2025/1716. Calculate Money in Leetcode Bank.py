class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        monday = 1
        
        while n > 0:
            week_days = min(n, 7)  
            ans += (week_days * (2 * monday + week_days - 1)) // 2
            n -= week_days
            monday += 1  
            
        return ans
