from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1map = Counter(s1)

        for i in range(len(s2) - len(s1) + 1):
            s2map = Counter(s2[i:i+len(s1)])
            if s1map == s2map:
                return True

        return False
