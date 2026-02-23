class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        seen = [0] * need
        mask = need - 1
        h = 0
        for i, c in enumerate(s):
            h = ((h << 1) & mask) | (c == '1')
            if i >= k-1 and not seen[h]:
                seen[h] = 1
                need -= 1
                if not need: return True
        return False
