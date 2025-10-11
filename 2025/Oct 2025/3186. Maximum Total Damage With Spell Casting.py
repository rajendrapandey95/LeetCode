from collections import Counter

class Solution:
    def maximumTotalDamage(self, power):
        count = Counter(power)
        keys = sorted(count.keys())
        n = len(keys)

        dp = [0] * (n + 1)  
        for i in range(1, n + 1):
            val = keys[i-1] * count[keys[i-1]]
            if i > 1 and keys[i-1] <= keys[i-2] + 2:
                dp[i] = max(dp[i-1], dp[i-2] + val)
            else:
                dp[i] = dp[i-1] + val
        return dp[n]
