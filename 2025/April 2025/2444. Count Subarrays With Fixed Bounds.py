class Solution:
    def countSubarrays(self, nums, minK, maxK):
        res = 0
        for i in range(len(nums)):
            mn = mx = nums[i]
            for j in range(i, len(nums)):
                mn = min(mn, nums[j])
                mx = max(mx, nums[j])
                res += mn == minK and mx == maxK
        return res
