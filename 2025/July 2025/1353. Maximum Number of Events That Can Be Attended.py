import heapq

class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        events.sort()
        pq, ans, j, n = [], 0, 0, len(events)
        for d in range(1, max(e[1] for e in events) + 1):
            while j < n and events[j][0] <= d:
                heapq.heappush(pq, events[j][1])
                j += 1
            while pq and pq[0] < d:
                heapq.heappop(pq)
            if pq:
                heapq.heappop(pq)
                ans += 1
        return ans
