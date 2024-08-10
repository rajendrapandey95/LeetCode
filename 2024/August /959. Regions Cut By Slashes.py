class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def regionsBySlashes(self, grid):
        grid_size = len(grid)
        expanded_size = grid_size * 3
        expanded_grid = [[0] * expanded_size for _ in range(expanded_size)]

        for i in range(grid_size):
            for j in range(grid_size):
                base_row, base_col = i * 3, j * 3
                if grid[i][j] == "\\":
                    expanded_grid[base_row][base_col] = expanded_grid[base_row + 1][base_col + 1] = expanded_grid[base_row + 2][base_col + 2] = 1
                elif grid[i][j] == "/":
                    expanded_grid[base_row][base_col + 2] = expanded_grid[base_row + 1][base_col + 1] = expanded_grid[base_row + 2][base_col] = 1

        region_count = 0
        for i in range(expanded_size):
            for j in range(expanded_size):
                if expanded_grid[i][j] == 0:
                    self._flood_fill(expanded_grid, i, j)
                    region_count += 1

        return region_count

    def _flood_fill(self, grid, row, col):
        queue = [(row, col)]
        grid[row][col] = 1
        while queue:
            r, c = queue.pop(0)
            for dr, dc in self.DIRECTIONS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid) and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr, nc))
