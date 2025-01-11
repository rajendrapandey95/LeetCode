class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        odd_count = sum(freq % 2 for freq in [s.count(chr(i)) for i in range(97, 123)])
        return odd_count <= k
