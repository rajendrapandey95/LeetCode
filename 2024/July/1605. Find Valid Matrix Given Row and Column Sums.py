class Solution:
    def restoreMatrix(self, rowSum, colSum):
        N, M = len(rowSum), len(colSum)
        curr_row_sum, curr_col_sum = [0] * N, [0] * M
        orig_matrix = [[0] * M for _ in range(N)]
        
        for i in range(N):
            for j in range(M):
                val = min(rowSum[i] - curr_row_sum[i], colSum[j] - curr_col_sum[j])
                orig_matrix[i][j] = val
                curr_row_sum[i] += val
                curr_col_sum[j] += val
        
        return orig_matrix
