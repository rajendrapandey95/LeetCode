from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s).values()
        return max(x for x in c if x % 2) - min(x for x in c if x % 2 == 0)
