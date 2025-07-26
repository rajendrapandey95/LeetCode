from typing import List

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        INF = 2**31 - 1
        bMin1, bMin2 = [INF] * (n + 1), [INF] * (n + 1)

        for a, b in conflictingPairs:
            if a > b:
                a, b = b, a
            if b < bMin1[a]:
                bMin2[a], bMin1[a] = bMin1[a], b
            elif b < bMin2[a]:
                bMin2[a] = b

        res, ib1, b2 = 0, n, 0x3FFFFFFF
        delCount = [0] * (n + 1)

        for i in range(n, 0, -1):
            if bMin1[ib1] > bMin1[i]:
                b2, ib1 = min(b2, bMin1[ib1]), i
            else:
                b2 = min(b2, bMin1[i])
            res += min(bMin1[ib1], n + 1) - i
            delCount[ib1] += min(min(b2, bMin2[ib1]), n + 1) - min(bMin1[ib1], n + 1)

        return res + max(delCount)
