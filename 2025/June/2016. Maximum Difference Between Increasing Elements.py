class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans, mn = -1, nums[0]
        for x in nums[1:]:
            if x > mn: ans = max(ans, x - mn)
            else: mn = x
        return ans
