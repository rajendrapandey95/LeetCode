class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        
        seats = [i for i, c in enumerate(corridor) if c == 'S']
        if len(seats) % 2 != 0 or len(seats) == 0:
            return 0
        
        ways = 1
        for i in range(1, len(seats) // 2):
            left = seats[2*i - 1]
            right = seats[2*i]
            ways = (ways * (right - left)) % MOD
        
        return ways
