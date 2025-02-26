class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_sum = max_sum = total = 0
        for num in nums:
            total += num
            min_sum = min(min_sum, total)
            max_sum = max(max_sum, total)
        return max_sum - min_sum
