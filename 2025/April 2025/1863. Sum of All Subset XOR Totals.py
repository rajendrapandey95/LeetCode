class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor_all = 0
        for num in nums:
            xor_all |= num
        return xor_all << (len(nums) - 1)
