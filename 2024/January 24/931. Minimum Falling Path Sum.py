from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        for row in range(1, n):
            for col in range(n):
                matrix[row][col] += min(
                    matrix[row-1][col],                                  
                    matrix[row-1][max(0, col-1)],                        
                    matrix[row-1][min(n-1, col+1)]                       
                )
        
        return min(matrix[-1])
