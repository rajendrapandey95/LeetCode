from collections import defaultdict

class Solution:
    def _isVowel(self, c: str) -> bool:
        return c in "aeiou"

    def _atLeastK(self, word: str, k: int) -> int:
        res, start, vowel_count, consonants = 0, 0, defaultdict(int), 0

        for end, c in enumerate(word):
            if self._isVowel(c):
                vowel_count[c] += 1
            else:
                consonants += 1

            while len(vowel_count) == 5 and consonants >= k:
                res += len(word) - end
                sc = word[start]
                if self._isVowel(sc):
                    vowel_count[sc] -= 1
                    if vowel_count[sc] == 0:
                        del vowel_count[sc]
                else:
                    consonants -= 1
                start += 1

        return res

    def countOfSubstrings(self, word: str, k: int) -> int:
        return self._atLeastK(word, k) - self._atLeastK(word, k + 1)
