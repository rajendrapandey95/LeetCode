from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def dfs(r, c):
            # Mark the current cell as visited
            visited.add((r, c))
            # Initialize boundaries of the farmland group
            top_left, bottom_right = [r, c], [r, c]
            
            # DFS in four directions
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and land[nr][nc] == 1 and (nr, nc) not in visited:
                    boundaries = dfs(nr, nc)
                    # Update boundaries based on the adjacent farmland group
                    top_left = [min(top_left[0], boundaries[0][0]), min(top_left[1], boundaries[0][1])]
                    bottom_right = [max(bottom_right[0], boundaries[1][0]), max(bottom_right[1], boundaries[1][1])]
            
            return [top_left, bottom_right]
        
        m, n = len(land), len(land[0])
        result = []
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1 and (i, j) not in visited:
                    farmland_group = dfs(i, j)
                    result.append([farmland_group[0][0], farmland_group[0][1], farmland_group[1][0], farmland_group[1][1]])
        
        return result
