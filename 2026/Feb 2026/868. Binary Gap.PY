class Solution:
    def binaryGap(self, N: int) -> int:
        prev = ans = -1
        i = 0
        while N:
            if N & 1:
                if prev != -1:
                    ans = max(ans, i - prev)
                prev = i
            N >>= 1
            i += 1
        return max(ans, 0)
