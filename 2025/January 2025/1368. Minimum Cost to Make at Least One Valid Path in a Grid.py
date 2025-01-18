class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        num_rows, num_cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        min_changes = [[float("inf")] * num_cols for _ in range(num_rows)]
        queue = deque([(0, 0, 0)])  
        
        while queue:
            row, col, cost = queue.popleft()
            if cost >= min_changes[row][col]:
                continue
            min_changes[row][col] = cost
            
            for i, (dr, dc) in enumerate(directions):
                nr, nc = row + dr, col + dc
                if 0 <= nr < num_rows and 0 <= nc < num_cols:
                    new_cost = cost + (1 if grid[row][col] != i + 1 else 0)
                    if new_cost < min_changes[nr][nc]:
                        if grid[row][col] == i + 1:
                            queue.appendleft((nr, nc, new_cost))
                        else:
                            queue.append((nr, nc, new_cost))
        
        return min_changes[-1][-1]
