from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        cmp = [0] * n

        for i in range(1, n):
            cmp[i] = cmp[i - 1] + (1 if nums[i] - nums[i - 1] > maxDiff else 0)

        res = []

        for u, v in queries:
            res.append(cmp[u] == cmp[v])

        return res
