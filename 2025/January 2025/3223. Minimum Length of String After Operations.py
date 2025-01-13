class Solution:
    def minimumLength(self, s: str) -> int:
        char_frequency = Counter(s)
        delete_count = sum(f - 1 if f % 2 else f - 2 for f in char_frequency.values())
        return len(s) - delete_count
