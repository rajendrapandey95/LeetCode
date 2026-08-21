class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:    
        def check(m):
            tot = 0
            for x in range(1, len(coins) + 1):
                for c in combinations(coins, x):
                    tot += m // lcm(*c) * pow(-1, x + 1)
            return tot >= k
    
        return bisect_left(range(k * coins[0] + 1), True, lo=1, key=check)
