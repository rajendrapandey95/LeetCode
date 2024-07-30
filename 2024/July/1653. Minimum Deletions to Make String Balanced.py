class Solution:
    def minimumDeletions(self, s: str) -> int:
        a = sum(1 for ch in s if ch == "a")
        b = 0
        min_del = len(s)
        for ch in s:
            if ch == "a":
                a -= 1
            min_del = min(min_del, a + b)
            if ch == "b":
                b += 1
        return min_del
