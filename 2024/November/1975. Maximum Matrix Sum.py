class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum, min_abs, neg_count = 0, float('inf'), 0
        for row in matrix:
            for val in row:
                total_sum += abs(val)
                min_abs = min(min_abs, abs(val))
                if val < 0:
                    neg_count += 1
        return total_sum - 2 * min_abs if neg_count % 2 else total_sum
