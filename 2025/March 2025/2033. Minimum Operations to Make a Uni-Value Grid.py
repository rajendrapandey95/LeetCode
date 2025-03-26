from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums_array = []
        result = float("inf")

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] % x != grid[0][0] % x:
                    return -1
                nums_array.append(grid[row][col])

        nums_array.sort()

        length = len(nums_array)
        prefix_sum = [0] * length
        suffix_sum = [0] * length

        for index in range(1, length):
            prefix_sum[index] = prefix_sum[index - 1] + nums_array[index - 1]

        for index in range(length - 2, -1, -1):
            suffix_sum[index] = suffix_sum[index + 1] + nums_array[index + 1]

        for index in range(length):
            left_operations = (nums_array[index] * index - prefix_sum[index]) // x
            right_operations = (suffix_sum[index] - nums_array[index] * (length - index - 1)) // x
            result = min(result, left_operations + right_operations)

        return result
