from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        mp=Counter(s)
        v=max((mp[c] for c in "aeiou" if c in mp),default=0)
        c=max((mp[c] for c in mp if c not in "aeiou"),default=0)
        return v+c
