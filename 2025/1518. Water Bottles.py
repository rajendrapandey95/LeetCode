class Solution:
    def numWaterBottles(self, n: int, x: int) -> int:
        return n + (n - 1) // (x - 1)
