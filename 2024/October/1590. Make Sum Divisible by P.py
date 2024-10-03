class Solution:
    def minSubarray(self, nums, p):
        total_sum = sum(nums) % p
        if total_sum == 0:
            return 0
        
        prefix = 0
        min_len, n, mods = len(nums), len(nums), {0: -1}
        
        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            target = (prefix - total_sum) % p
            if target in mods:
                min_len = min(min_len, i - mods[target])
            mods[prefix] = i

        return min_len if min_len < n else -1
