class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        total_sum, prefix_sum, count = sum(nums), 0, 0

        for i in range(len(nums) - 1):
            prefix_sum += nums[i]
            if prefix_sum >= total_sum - prefix_sum:
                count += 1

        return count
