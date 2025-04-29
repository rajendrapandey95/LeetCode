class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        ans = start = count = 0
        for end, x in enumerate(nums):
            if x == max_val:
                count += 1
            while count == k:
                if nums[start] == max_val:
                    count -= 1
                start += 1
            ans += start
        return ans
