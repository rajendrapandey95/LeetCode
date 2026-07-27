class Solution:
    def maxProduct(self, nums):
        nums.sort(reverse=True)
        
        result = (nums[0] - 1) * (nums[1] - 1)
        
        return result
