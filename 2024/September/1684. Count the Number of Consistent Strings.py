class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        return sum(all(char in allowed_set for char in word) for word in words)
