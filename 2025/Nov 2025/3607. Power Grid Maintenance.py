class DSU:
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def join(self, a, b):
        self.p[self.find(b)] = self.find(a)


class Solution:
    def processQueries(self, c, connections, queries):
        dsu = DSU(c+1)
        for u, v in connections:
            dsu.join(u, v)

        online = [1]*(c+1)
        cnt = [0]*(c+1)
        best = {}

        for op, x in queries:
            if op == 2:
                online[x] = 0
                cnt[x] += 1

        for i in range(1, c+1):
            r = dsu.find(i)
            if r not in best: best[r] = -1
            if online[i]:
                best[r] = i if best[r] == -1 else min(best[r], i)

        ans = []
        for op, x in reversed(queries):
            r = dsu.find(x)
            cur = best[r]

            if op == 1:
                ans.append(x if online[x] else cur)

            else: 
                if cnt[x] > 1:
                    cnt[x] -= 1
                else:
                    online[x] = 1
                    best[r] = x if cur == -1 else min(cur, x)

        return ans[::-1]
