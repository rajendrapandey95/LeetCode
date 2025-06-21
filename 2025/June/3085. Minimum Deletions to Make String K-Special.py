from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = list(Counter(word).values())
        ans = len(word)
        for a in freq:
            d = sum(b if b < a else max(0, b - a - k) for b in freq)
            ans = min(ans, d)
        return ans
