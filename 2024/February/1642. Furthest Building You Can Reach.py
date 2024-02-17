import heapq

class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        diffs = []  
        total_bricks = 0
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(diffs, diff)
                if len(diffs) > ladders:  
                    total_bricks += heapq.heappop(diffs)
                if total_bricks > bricks:  
                    return i
        return len(heights) - 1
