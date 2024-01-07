from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        total_count = 0

        for i in range(2, n):
            for j in range(i - 1, -1, -1):
                if 2 * nums[j] == nums[i] + nums[j - 1]:
                    dp[i] += dp[j] + 1

            total_count += dp[i]

        return total_count
