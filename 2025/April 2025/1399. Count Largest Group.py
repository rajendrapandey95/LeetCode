class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import Counter
        cnt = Counter(sum(map(int, str(i))) for i in range(1, n + 1))
        maxFreq = max(cnt.values())
        return sum(v == maxFreq for v in cnt.values())
