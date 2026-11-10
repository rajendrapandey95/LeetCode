class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        costs = [0] + costs
        a, b, c = costs[n], inf, inf 
        for i in reversed(range(n)):
            a, b, c = costs[i] + min(a + 1, b + 4, c + 9), a, b
        return a
