class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        max_identical_rows = 0
        for row in matrix:
            flipped = [1 - x for x in row]
            max_identical_rows = max(max_identical_rows, sum(1 for r in matrix if r == row or r == flipped))
        return max_identical_rows
