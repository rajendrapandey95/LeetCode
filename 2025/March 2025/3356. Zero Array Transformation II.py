from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        left, right = 0, len(queries)

        if not self._can_form_zero_array(nums, queries, right):
            return -1

        while left < right:
            mid = (left + right) // 2
            if self._can_form_zero_array(nums, queries, mid):
                right = mid
            else:
                left = mid + 1

        return left

    def _can_form_zero_array(self, nums: List[int], queries: List[List[int]], k: int) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        total = 0

        for i in range(k):
            start, end, val = queries[i]
            diff[start] += val
            diff[end + 1] -= val

        for i in range(n):
            total += diff[i]
            if total < nums[i]:
                return False

        return True
