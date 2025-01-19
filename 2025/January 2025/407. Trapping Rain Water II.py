class Solution:
    def trapRainWater(self, height_map: List[List[int]]) -> int:
        from heapq import heappush, heappop
        
        if not height_map or not height_map[0]:
            return 0

        num_rows, num_cols = len(height_map), len(height_map[0])
        visited = [[False] * num_cols for _ in range(num_rows)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        boundary = []

        for r in range(num_rows):
            for c in (0, num_cols - 1):
                heappush(boundary, (height_map[r][c], r, c))
                visited[r][c] = True
        for c in range(num_cols):
            for r in (0, num_rows - 1):
                heappush(boundary, (height_map[r][c], r, c))
                visited[r][c] = True

        total_water = 0

        while boundary:
            height, row, col = heappop(boundary)
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < num_rows and 0 <= nc < num_cols and not visited[nr][nc]:
                    visited[nr][nc] = True
                    total_water += max(0, height - height_map[nr][nc])
                    heappush(boundary, (max(height, height_map[nr][nc]), nr, nc))

        return total_water
