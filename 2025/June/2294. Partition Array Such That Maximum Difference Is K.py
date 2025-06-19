class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans, rec = 1, nums[0]
        for x in nums:
            if x - rec > k:
                ans += 1
                rec = x
        return ans
