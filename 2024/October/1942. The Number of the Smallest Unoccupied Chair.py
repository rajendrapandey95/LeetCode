class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = [[t[0], i] for i, t in enumerate(times)] + [[t[1], ~i] for i, t in enumerate(times)]
        events.sort()
        free = list(range(len(times)))
        occ = []

        for t, f in events:
            while occ and occ[0][0] <= t:
                heapq.heappush(free, heapq.heappop(occ)[1])
            if f >= 0:
                chair = heapq.heappop(free)
                if f == targetFriend:
                    return chair
                heapq.heappush(occ, [times[f][1], chair])
