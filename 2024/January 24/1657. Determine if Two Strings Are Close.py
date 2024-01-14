class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Check if the sets of characters are equal
        if set(word1) != set(word2):
            return False

        # Check if the sets of frequencies are equal
        freq1 = [word1.count(c) for c in set(word1)]
        freq2 = [word2.count(c) for c in set(word2)]
        freq1.sort()
        freq2.sort()

        return freq1 == freq2
