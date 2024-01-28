from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])
        
        # Calculate the prefix sum for each row
        for row in matrix:
            for j in range(1, cols):
                row[j] += row[j - 1]
        
        result = 0
        
        # Iterate through all possible pairs of columns
        for col1 in range(cols):
            for col2 in range(col1, cols):
                # Use a defaultdict to store the count of prefix sums
                prefix_sum_count = defaultdict(int)
                prefix_sum_count[0] = 1
                current_sum = 0
                
                # Iterate through each row and calculate the prefix sum
                for row in matrix:
                    current_sum += row[col2] - (row[col1 - 1] if col1 > 0 else 0)
                    result += prefix_sum_count[current_sum - target]
                    prefix_sum_count[current_sum] += 1
        
        return result
