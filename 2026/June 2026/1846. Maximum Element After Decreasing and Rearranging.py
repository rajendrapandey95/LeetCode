from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        n = len(arr)
        for i in range(1, n):
            arr[i] = min(arr[i], arr[i - 1] + 1)
        return max(arr)
