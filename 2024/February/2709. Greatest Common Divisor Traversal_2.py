class Solution:
    def canTraverseAllPairs(self, nums):
        MAX = 100000
        N = len(nums)
        has = [False] * (MAX + 1)
        for x in nums:
            has[x] = True

        # Edge cases
        if N == 1:
            return True
        if has[1]:
            return False

        # Prime sieve optimization
        sieve = [0] * (MAX + 1)
        for d in range(2, int(MAX ** 0.5) + 1):
            if sieve[d] == 0:
                for v in range(d * d, MAX + 1, d):
                    sieve[v] = d
        for d in range(2, MAX + 1):
            if sieve[d] == 0:
                sieve[d] = d

        # Union-Find initialization
        union = DSU(2 * MAX + 1)

        # Traverse nums
        for x in nums:
            val = x
            while val > 1:
                prime = sieve[val]
                root = prime + MAX
                if union.find(root) != union.find(x):
                    union.merge(root, x)
                while val % prime == 0:
                    val //= prime

        cnt = 0
        for i in range(2, MAX + 1):
            if has[i] and union.find(i) == i:
                cnt += 1
                if cnt > 1:  # Early termination
                    return False
        return cnt == 1


class DSU:
    def __init__(self, N):
        self.dsu = list(range(N + 1))
        self.size = [1] * (N + 1)

    def find(self, x):
        if self.dsu[x] == x:
            return x
        self.dsu[x] = self.find(self.dsu[x])
        return self.dsu[x]

    def merge(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx == fy:
            return
        if self.size[fx] > self.size[fy]:
            fx, fy = fy, fx
        self.dsu[fx] = fy
        self.size[fy] += self.size[fx]
