from typing import List, Tuple

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[bool]:
        ans = [False] * len(queries)
        violating_indices = []

        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                violating_indices.append(i)

        for i, (start, end) in enumerate(queries):
            found_violating_index = self.binarySearch(start + 1, end, violating_indices)
            ans[i] = not found_violating_index

        return ans

    def binarySearch(self, start: int, end: int, violating_indices: List[int]) -> bool:
        left, right = 0, len(violating_indices) - 1
        while left <= right:
            mid = left + (right - left) // 2
            violating_index = violating_indices[mid]

            if violating_index < start:
                left = mid + 1
            elif violating_index > end:
                right = mid - 1
            else:
                return True

        return False
