class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        max_count = [0]
        self.backtrack(s, 0, set(), 0, max_count)
        return max_count[0]

    def backtrack(self, s: str, start: int, seen: set, count: int, max_count: list) -> None:
        if count + len(s) - start <= max_count[0]:
            return
        if start == len(s):
            max_count[0] = max(max_count[0], count)
            return
        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]
            if sub not in seen:
                seen.add(sub)
                self.backtrack(s, end, seen, count + 1, max_count)
                seen.remove(sub)
