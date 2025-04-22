MOD = 10**9 + 7
MAX = 10**4 + 15

sieve = [0] * MAX
for i in range(2, MAX):
    if sieve[i] == 0:
        for j in range(i, MAX, i):
            sieve[j] = i

ps = [[] for _ in range(MAX)]
for i in range(2, MAX):
    x = i
    while x > 1:
        p, cnt = sieve[x], 0
        while x % p == 0: x //= p; cnt += 1
        ps[i].append(cnt)

C = [[1] + [0]*15 for _ in range(MAX)]
for i in range(1, MAX):
    for j in range(1, 16):
        C[i][j] = (C[i-1][j] + C[i-1][j-1]) % MOD

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        res = 0
        for x in range(1, maxValue + 1):
            ways = 1
            for p in ps[x]:
                ways = ways * C[n + p - 1][p] % MOD
            res = (res + ways) % MOD
        return res
