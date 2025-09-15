from typing import Set

class Solution:
    def canBeTypedWords(self, text: str, broken: str) -> int:
        brokenKeys: Set[str] = set(broken)
        words = text.split()
        count = 0

        for word in words:
            for c in word:
                if c in brokenKeys:
                    count += 1
                    break

        return len(words) - count
