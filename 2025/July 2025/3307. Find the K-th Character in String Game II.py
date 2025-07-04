class Solution:
    def kthCharacter(self, k: int, ops: list[int]) -> str:
        ans, k = 0, k - 1
        for i in range(k.bit_length() - 1, -1, -1):
            ans += ops[i] if (k >> i) & 1 else 0
        return chr(ord('a') + ans % 26)
