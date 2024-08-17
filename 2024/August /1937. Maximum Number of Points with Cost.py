class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        prev_row = points[0]

        for row in range(1, rows):
            left_max = prev_row[:]
            right_max = prev_row[:]

            for col in range(1, cols):
                left_max[col] = max(left_max[col - 1] - 1, prev_row[col])

            for col in range(cols - 2, -1, -1):
                right_max[col] = max(right_max[col + 1] - 1, prev_row[col])

            prev_row = [points[row][col] + max(left_max[col], right_max[col]) for col in range(cols)]

        return max(prev_row)
