class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            x = nums[i]
            res = -1
            d = 1
            while d < x:
                if x & d:
                    res = x - d
                    break
                d <<= 1
            nums[i] = res
        return nums
