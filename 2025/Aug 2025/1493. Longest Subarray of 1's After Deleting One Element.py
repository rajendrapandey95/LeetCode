class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero, start, ans = 0, 0, 0
        for i, v in enumerate(nums):
            if v == 0: 
                zero += 1
            while zero > 1:
                if nums[start] == 0: 
                    zero -= 1
                start += 1
            ans = max(ans, i - start)
        return ans
