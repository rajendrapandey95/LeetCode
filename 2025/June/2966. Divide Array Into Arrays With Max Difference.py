class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        return [[nums[i], nums[i+1], nums[i+2]] for i in range(0, len(nums), 3) if nums[i+2] - nums[i] <= k] if all(nums[i+2] - nums[i] <= k for i in range(0, len(nums), 3)) else []
