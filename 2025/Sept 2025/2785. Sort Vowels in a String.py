class Solution:
    def sortVowels(self, s: str) -> str:
        v=[c for c in s if c in "aeiouAEIOU"]
        v.sort()
        it=iter(v)
        return ''.join(next(it) if c in "aeiouAEIOU" else c for c in s)
