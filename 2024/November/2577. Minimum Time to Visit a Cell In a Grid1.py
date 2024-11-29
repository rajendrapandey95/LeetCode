import heapq
from typing import List

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        
        pq = [(grid[0][0], 0, 0)]  
        
        while pq:
            time, row, col = heapq.heappop(pq)
            
            if (row, col) == (rows - 1, cols - 1):
                return time
            
            if (row, col) in visited:
                continue
            visited.add((row, col))
            
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                
                if 0 <= next_row < rows and 0 <= next_col < cols and (next_row, next_col) not in visited:
                    wait_time = 1 if (grid[next_row][next_col] - time) % 2 == 0 else 0
                    next_time = max(grid[next_row][next_col] + wait_time, time + 1)
                    
                    heapq.heappush(pq, (next_time, next_row, next_col))
        
        return -1

