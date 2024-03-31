class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        mink_idx = -1
        maxk_idx = -1
        bad_idx =  -1
        ans = 0
        for i in range(len(nums)):
            if not (minK<=nums[i] and nums[i]<= maxK): bad_idx = i
            if nums[i] == minK: mink_idx = i
            if nums[i] == maxK: maxk_idx = i
            ans += max(0, min(maxk_idx, mink_idx) - bad_idx)
        return ans
