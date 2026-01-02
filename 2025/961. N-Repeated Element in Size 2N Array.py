class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        seen = set()
        for x in A:
            if x in seen:
                return x
            seen.add(x)
