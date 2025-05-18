from collections import defaultdict

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        base = 3**m
        valid = {}
        
        for mask in range(base):
            colors, tmp = [], mask
            for _ in range(m):
                colors.append(tmp % 3)
                tmp //= 3
            if all(colors[i] != colors[i+1] for i in range(m - 1)):
                valid[mask] = colors

        adj = defaultdict(list)
        for a, ca in valid.items():
            for b, cb in valid.items():
                if all(x != y for x, y in zip(ca, cb)):
                    adj[a].append(b)

        dp = [int(i in valid) for i in range(base)]
        for _ in range(1, n):
            ndp = [0] * base
            for b in valid:
                ndp[b] = sum(dp[a] for a in adj[b]) % MOD
            dp = ndp

        return sum(dp) % MOD
