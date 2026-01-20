class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i, x in enumerate(nums):
            nums[i] = x - (x & -x) if x else -1
        return nums
