import heapq
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])  
        pq, max_val, max_sum = [], 0, 0

        for start, end, value in events:
            while pq and pq[0][0] < start:
                max_val = max(max_val, heapq.heappop(pq)[1])
            max_sum = max(max_sum, max_val + value)
            heapq.heappush(pq, (end, value))

        return max_sum
