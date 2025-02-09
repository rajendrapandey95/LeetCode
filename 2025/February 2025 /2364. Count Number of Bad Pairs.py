from collections import defaultdict

class Solution:
    def countBadPairs(self, nums):
        n = len(nums)
        total_pairs = n * (n - 1) // 2 
        diff_count = defaultdict(int)
        good_pairs = 0

        for i, num in enumerate(nums):
            diff = i - num
            good_pairs += diff_count[diff]  
            diff_count[diff] += 1

        return total_pairs - good_pairs
