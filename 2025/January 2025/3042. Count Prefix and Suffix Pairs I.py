class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        return sum(1 for i, w1 in enumerate(words) for w2 in words[i+1:] if len(w1) <= len(w2) and w2.startswith(w1) and w2.endswith(w1))
