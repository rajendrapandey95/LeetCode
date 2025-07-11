from heapq import heappush, heappop, heapify

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        free, busy = list(range(n)), []
        heapify(free)
        cnt = [0] * n
        for s, e in sorted(meetings):
            while busy and busy[0][0] <= s:
                _, r = heappop(busy)
                heappush(free, r)
            if free:
                r = heappop(free)
                heappush(busy, [e, r])
            else:
                t, r = heappop(busy)
                heappush(busy, [t + e - s, r])
            cnt[r] += 1
        return cnt.index(max(cnt))
