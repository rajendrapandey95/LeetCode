class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        target = total // 2
        dp = [True] + [False] * target
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]
        return dp[target]
