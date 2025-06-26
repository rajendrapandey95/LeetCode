class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        sm = cnt = 0
        bits = k.bit_length()
        for i, ch in enumerate(reversed(s)):
            if ch == "0" or (i < bits and sm + (1 << i) <= k):
                cnt += 1
                sm += (1 << i) * (ch == "1")
        return cnt
