from heapq import heappush, heappop
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        shortest_length = float("inf")
        cumulative_sum = 0
        prefix_sum_heap = []

        for i, num in enumerate(nums):
            cumulative_sum += num

            if cumulative_sum >= k:
                shortest_length = min(shortest_length, i + 1)

            while prefix_sum_heap and cumulative_sum - prefix_sum_heap[0][0] >= k:
                _, index = heappop(prefix_sum_heap)
                shortest_length = min(shortest_length, i - index)

            heappush(prefix_sum_heap, (cumulative_sum, i))

        return -1 if shortest_length == float("inf") else shortest_length
