class Solution:
    def minimumCost(self, S, T, A, B, C):
        INF = 10**18

        ch = [[-1]*26]
        idd = [-1]
        nid = 0

        def add(w):
            nonlocal nid
            u = 0
            for c in w:
                x = ord(c) - 97
                if ch[u][x] < 0:
                    ch[u][x] = len(ch)
                    ch.append([-1]*26)
                    idd.append(-1)
                u = ch[u][x]
            if idd[u] < 0:
                idd[u] = nid
                nid += 1
            return idd[u]

        edges = []
        for a, b, c in zip(A, B, C):
            edges.append((add(a), add(b), c))

        if nid == 0:
            return 0 if S == T else -1

        d = [[INF]*nid for _ in range(nid)]
        for i in range(nid):
            d[i][i] = 0
        for x, y, w in edges:
            d[x][y] = min(d[x][y], w)

        for k in range(nid):
            for i in range(nid):
                if d[i][k] == INF: continue
                for j in range(nid):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

        n = len(S)
        dp = [INF]*(n+1)
        dp[0] = 0
        s = [ord(c)-97 for c in S]
        t = [ord(c)-97 for c in T]

        for i in range(n):
            if dp[i] == INF: continue
            if S[i] == T[i]:
                dp[i+1] = min(dp[i+1], dp[i])

            u = v = 0
            for j in range(i, n):
                u = ch[u][s[j]]
                v = ch[v][t[j]]
                if u < 0 or v < 0: break
                if idd[u] >= 0 and idd[v] >= 0:
                    dp[j+1] = min(dp[j+1], dp[i] + d[idd[u]][idd[v]])

        return -1 if dp[n] == INF else dp[n]
