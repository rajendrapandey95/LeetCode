import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq, result = [], []
        
        if a > 0:
            heapq.heappush(pq, (-a, "a"))
        if b > 0:
            heapq.heappush(pq, (-b, "b"))
        if c > 0:
            heapq.heappush(pq, (-c, "c"))

        while pq:
            count, char = heapq.heappop(pq)
            count = -count
            if len(result) >= 2 and result[-1] == char and result[-2] == char:
                if not pq:
                    break
                tempCnt, tempChar = heapq.heappop(pq)
                result.append(tempChar)
                if (tempCnt + 1) < 0:
                    heapq.heappush(pq, (tempCnt + 1, tempChar))
                heapq.heappush(pq, (-count, char))
            else:
                result.append(char)
                if count > 1:
                    heapq.heappush(pq, (-(count - 1), char))

        return "".join(result)
