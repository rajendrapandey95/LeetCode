import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h, s = [1], {1}
        for _ in range(n):
            u = heapq.heappop(h)
            for m in (2, 3, 5):
                nxt = u * m
                if nxt not in s:
                    s.add(nxt)
                    heapq.heappush(h, nxt)
        return u
