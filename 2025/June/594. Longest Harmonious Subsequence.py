class Solution:
    def findLHS(self, nums):
        nums.sort()
        j = res = 0
        for i in range(len(nums)):
            while nums[i] - nums[j] > 1: j += 1
            if nums[i] - nums[j] == 1:
                res = max(res, i - j + 1)
        return res
