class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        cnt = [0] * 26
        for ch in s: cnt[ord(ch) - 97] += 1
        for _ in range(t):
            cnt = [(cnt[-1] + cnt[0]) % mod] + [cnt[-1]] + cnt[1:25]
        return sum(cnt) % mod
