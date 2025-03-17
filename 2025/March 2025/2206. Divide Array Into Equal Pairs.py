class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(nums[i] == nums[i + 1] for i in range(0, len(nums), 2)) if not (len(nums) % 2) and nums.sort() else False
