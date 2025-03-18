class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        used, start, res = 0, 0, 0
        for end in range(len(nums)):
            while used & nums[end]: 
                used ^= nums[start]
                start += 1
            used |= nums[end]
            res = max(res, end - start + 1)
        return res
