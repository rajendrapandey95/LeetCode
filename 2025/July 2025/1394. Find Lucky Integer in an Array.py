class Solution:
    def findLucky(self, arr: list[int]) -> int:
        from collections import Counter
        return max((x for x, c in Counter(arr).items() if x == c), default=-1)
