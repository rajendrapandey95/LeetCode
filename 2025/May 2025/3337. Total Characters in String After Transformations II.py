MOD = 10**9 + 7
L = 26

class Mat:
    def __init__(self, copy=None):
        self.a = [[0]*L for _ in range(L)]
        if copy:
            for i in range(L):
                self.a[i] = copy.a[i][:]

    def __mul__(self, o):
        r = Mat()
        for i in range(L):
            for j in range(L):
                r.a[i][j] = sum(self.a[i][k]*o.a[k][j] for k in range(L)) % MOD
        return r

def I():
    m = Mat()
    for i in range(L): m.a[i][i] = 1
    return m

def quickmul(x, y):
    r = I()
    while y:
        if y & 1: r = r * x
        x = x * x
        y >>= 1
    return r

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        T = Mat()
        for i in range(L):
            for j in range(1, nums[i]+1):
                T.a[(i + j) % L][i] = 1
        T = quickmul(T, t)

        f = [0]*L
        for c in s: f[ord(c)-97] += 1

        return sum(T.a[i][j]*f[j] for i in range(L) for j in range(L)) % MOD
