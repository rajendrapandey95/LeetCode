from math import inf

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = energy[:]  
        ans = -inf

        for i in range(n - 1 - k, -1, -1):
            dp[i] += dp[i + k]
        
        return max(dp[n - k:])  
