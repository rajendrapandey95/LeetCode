class Solution:
    UNGUARDED = 0
    GUARDED = 1
    GUARD = 2
    WALL = 3

    def _mark_guarded(self, row: int, col: int, grid: List[List[int]]) -> None:
        for r in range(row - 1, -1, -1):  # Up
            if grid[r][col] in {self.WALL, self.GUARD}:
                break
            grid[r][col] = self.GUARDED

        for r in range(row + 1, len(grid)):  # Down
            if grid[r][col] in {self.WALL, self.GUARD}:
                break
            grid[r][col] = self.GUARDED

        for c in range(col - 1, -1, -1):  # Left
            if grid[row][c] in {self.WALL, self.GUARD}:
                break
            grid[row][c] = self.GUARDED

        for c in range(col + 1, len(grid[0])):  # Right
            if grid[row][c] in {self.WALL, self.GUARD}:
                break
            grid[row][c] = self.GUARDED

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[self.UNGUARDED] * n for _ in range(m)]

        for guard in guards:  # Place guards
            grid[guard[0]][guard[1]] = self.GUARD

        for wall in walls:  # Place walls
            grid[wall[0]][wall[1]] = self.WALL

        for guard in guards:  # Mark guarded areas
            self._mark_guarded(guard[0], guard[1], grid)

        return sum(cell == self.UNGUARDED for row in grid for cell in row)
