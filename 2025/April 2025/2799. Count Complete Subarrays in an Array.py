class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        from collections import Counter
        n, total, d = len(nums), 0, len(set(nums))
        cnt, r = Counter(), 0
        for l in range(n):
            if l: 
                cnt[nums[l-1]] -= 1
                if cnt[nums[l-1]] == 0: del cnt[nums[l-1]]
            while r < n and len(cnt) < d:
                cnt[nums[r]] += 1
                r += 1
            if len(cnt) == d: total += n - r + 1
        return total
