class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = total = i = 0
        for j, x in enumerate(nums):
            total += x
            while total * (j - i + 1) >= k:
                total -= nums[i]
                i += 1
            res += j - i + 1
        return res
