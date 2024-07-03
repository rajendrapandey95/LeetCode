class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 4:
            return 0

        nums.sort()

        min_diff = float("inf")

        for i in range(4):
            min_diff = min(min_diff, nums[n - 4 + i] - nums[i])

        return min_diff
