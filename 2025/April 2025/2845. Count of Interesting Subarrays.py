class Solution:
    def countInterestingSubarrays(self, nums: List[int], mod: int, k: int) -> int:
        from collections import Counter
        cnt = Counter([0])
        res = pre = 0
        for x in nums:
            pre += x % mod == k
            res += cnt[(pre - k) % mod]
            cnt[pre % mod] += 1
        return res
