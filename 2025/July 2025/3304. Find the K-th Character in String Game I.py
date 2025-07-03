class Solution:
    def kthCharacter(self, k: int) -> str:
        ans = 0
        while k > 1:
            t = k.bit_length() - (k & (k - 1) == 0)
            k -= 1 << (t - 1)
            ans += 1
        return chr(ord('a') + ans)
