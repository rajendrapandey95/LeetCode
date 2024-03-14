from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Initialize variables
        count = 0
        prefix_sums = [0]
        sum_count = {0: 1}
        
        # Compute prefix sums and store their frequencies
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)
            if prefix_sums[-1] - goal in sum_count:
                count += sum_count[prefix_sums[-1] - goal]
            if prefix_sums[-1] in sum_count:
                sum_count[prefix_sums[-1]] += 1
            else:
                sum_count[prefix_sums[-1]] = 1
        
        return count
