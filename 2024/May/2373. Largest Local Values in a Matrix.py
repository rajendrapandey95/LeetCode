class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                max_val = float('-inf')
                for x in range(3):
                    for y in range(3):
                        max_val = max(max_val, grid[i + x][j + y])
                maxLocal[i][j] = max_val
        
        return maxLocal
