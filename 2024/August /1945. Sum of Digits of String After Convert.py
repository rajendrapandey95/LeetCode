class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = sum(int(d) for ch in s for d in str(ord(ch) - ord('a') + 1))

        for _ in range(k - 1):
            num = sum(int(d) for d in str(num))
        
        return num
