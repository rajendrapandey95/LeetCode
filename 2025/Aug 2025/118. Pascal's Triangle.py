from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for _ in range(1, numRows):
            prev = result[-1]
            # Generate new row using previous row
            row = [1] + [prev[i] + prev[i + 1] for i in range(len(prev) - 1)] + [1]
            result.append(row)
        return result
