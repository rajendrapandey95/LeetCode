class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        num_rows, num_cols = len(mat), len(mat[0])
        row_count, col_count = [0] * num_rows, [0] * num_cols
        num_to_pos = {mat[r][c]: (r, c) for r in range(num_rows) for c in range(num_cols)}

        for i, num in enumerate(arr):
            row, col = num_to_pos[num]
            row_count[row] += 1
            col_count[col] += 1

            if row_count[row] == num_cols or col_count[col] == num_rows:
                return i

        return -1
