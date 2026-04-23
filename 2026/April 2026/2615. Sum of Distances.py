class Solution:
    def distance(self, nums):
        from collections import defaultdict

        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)

        res = [0] * len(nums)

        for g in pos.values():
            total = sum(g)
            pref = 0
            k = len(g)

            for i, idx in enumerate(g):
                res[idx] = total - 2 * pref + idx * (2 * i - k)
                pref += idx

        return res
