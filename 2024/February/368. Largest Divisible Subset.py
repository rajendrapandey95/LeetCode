from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        nums.sort()
        n = len(nums)
        dp = [1] * n  # dp[i] stores the length of the largest subset ending at nums[i]
        parent = [-1] * n  # parent[i] stores the index of the previous element in the largest subset ending at nums[i]
        max_len = 1
        max_index = 0
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                    if dp[i] > max_len:
                        max_len = dp[i]
                        max_index = i
        
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = parent[max_index]
        
        return result[::-1]  # Reversing the result to get the subset in ascending order
