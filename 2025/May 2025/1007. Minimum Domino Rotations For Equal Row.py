class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def getRotations(target):
            top = bottom = 0
            for a, b in zip(tops, bottoms):
                if a != target and b != target:
                    return float('inf')
                if a != target: top += 1
                if b != target: bottom += 1
            return min(top, bottom)

        res = getRotations(tops[0])
        if tops[0] != bottoms[0]:
            res = min(res, getRotations(bottoms[0]))
        return -1 if res == float('inf') else res
