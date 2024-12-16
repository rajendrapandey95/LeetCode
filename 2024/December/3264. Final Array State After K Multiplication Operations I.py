class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        for _ in range(k):
            nums[nums.index(min(nums))] *= multiplier
        return nums
