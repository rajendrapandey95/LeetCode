from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        
        dp = [0] * len(jobs)
        dp[0] = jobs[0][2]  
        
        for i in range(1, len(jobs)):
            latestNonOverlap = self.findLatestNonOverlap(jobs, i)
            
            includingProfit = jobs[i][2] + (dp[latestNonOverlap] if latestNonOverlap != -1 else 0)
            excludingProfit = dp[i-1]
            dp[i] = max(includingProfit, excludingProfit)
        
        return dp[-1]

    def findLatestNonOverlap(self, jobs, index):
        start, end = 0, index - 1
        while start <= end:
            mid = (start + end) // 2
            if jobs[mid][1] <= jobs[index][0]:
                if jobs[mid + 1][1] <= jobs[index][0]:
                    start = mid + 1
                else:
                    return mid
            else:
                end = mid - 1
        return -1
