class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = [s[i:i+k] for i in range(0, len(s), k)]
        res[-1] += fill * (k - len(res[-1]))
        return res
