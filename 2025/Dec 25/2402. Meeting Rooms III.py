from heapq import heappush, heappop, heapify
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        free = list(range(n))
        heapify(free)
        
        busy = [] 
        count = [0] * n
        
        for start, end in meetings:
            while busy and busy[0][0] <= start:
                _, room = heappop(busy)
                heappush(free, room)
            
            if free:
                room = heappop(free)
                heappush(busy, (end, room))
            else:
                end_time, room = heappop(busy)
                duration = end - start
                heappush(busy, (end_time + duration, room))
            
            count[room] += 1
        
        return count.index(max(count))
