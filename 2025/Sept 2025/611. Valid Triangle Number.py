from typing import List
import bisect

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n - 2):
            if nums[i] == 0:
                continue
            k = i + 2
            for j in range(i + 1, n - 1):
                idx = bisect.bisect_left(nums, nums[i] + nums[j], k, n)
                count += idx - j - 1
        return count
