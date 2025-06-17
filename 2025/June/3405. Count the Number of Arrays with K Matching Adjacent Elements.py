MOD, MX = 10**9 + 7, 10**5
fact = [0] * MX
inv = [0] * MX

def qpow(x, n):
    r = 1
    while n:
        if n & 1: r = r * x % MOD
        x = x * x % MOD
        n >>= 1
    return r

def init():
    if fact[0]: return
    fact[0] = 1
    for i in range(1, MX):
        fact[i] = fact[i - 1] * i % MOD
    inv[-1] = qpow(fact[-1], MOD - 2)
    for i in range(MX - 2, -1, -1):
        inv[i] = inv[i + 1] * (i + 1) % MOD

def C(n, k):
    return fact[n] * inv[k] % MOD * inv[n - k] % MOD

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        init()
        return C(n - 1, k) * m % MOD * qpow(m - 1, n - k - 1) % MOD
