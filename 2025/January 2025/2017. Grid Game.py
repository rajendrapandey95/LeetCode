class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        first_row_sum, second_row_sum, minimum_sum = sum(grid[0]), 0, float("inf")
        for i in range(len(grid[0])):
            first_row_sum -= grid[0][i]
            minimum_sum = min(minimum_sum, max(first_row_sum, second_row_sum))
            second_row_sum += grid[1][i]
        return minimum_sum
