class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total = sum(range(1, n * n + 1))
        total_sq = sum(x * x for x in range(1, n * n + 1))

        sum_grid = sum(sum(row) for row in grid)
        sum_grid_sq = sum(x * x for row in grid for x in row)

        diff = sum_grid - total 
        sum_diff = (sum_grid_sq - total_sq) // diff 

        X = (diff + sum_diff) // 2  
        Y = sum_diff - X  
        return [X, Y]
