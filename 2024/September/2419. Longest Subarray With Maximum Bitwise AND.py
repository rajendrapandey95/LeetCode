class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mv = ans = cs = 0
        for n in nums:
            if mv < n:
                mv = n
                ans = cs = 0
            if mv == n:
                cs += 1
            else:
                cs = 0
            ans = max(ans, cs)
        return ans
