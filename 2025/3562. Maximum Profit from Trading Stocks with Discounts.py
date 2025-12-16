class Solution:
    def maxProfit(self, n, present, future, hierarchy, budget):
        g = [[] for _ in range(n)]
        for u, v in hierarchy:
            g[u - 1].append(v - 1)

        def dfs(u):
            cost, dcost = present[u], present[u] // 2
            dp0 = dp1 = [0] * (budget + 1)
            sub0 = sub1 = [0] * (budget + 1)
            size = cost

            for v in g[u]:
                c0, c1, csize = dfs(v)
                size += csize
                for i in range(budget, -1, -1):
                    for s in range(min(csize, i) + 1):
                        sub0[i] = max(sub0[i], sub0[i - s] + c0[s])
                        sub1[i] = max(sub1[i], sub1[i - s] + c1[s])

            dp0, dp1 = sub0[:], sub0[:]
            gain = future[u]

            for i in range(budget + 1):
                if i >= cost:
                    dp0[i] = max(dp0[i], sub1[i - cost] + gain - cost)
                if i >= dcost:
                    dp1[i] = max(dp1[i], sub1[i - dcost] + gain - dcost)

            return dp0, dp1, size

        return dfs(0)[0][budget]
