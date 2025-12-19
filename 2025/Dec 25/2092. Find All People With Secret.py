class Solution:
    def findAllPeople(self, n, meetings, firstPerson):
        from collections import defaultdict, deque
        INF = 10**18

        g = defaultdict(list)
        for x, y, t in meetings:
            g[x].append((t, y))
            g[y].append((t, x))

        time = [INF]*n
        time[0] = time[firstPerson] = 0

        q = deque([(0, 0), (firstPerson, 0)])

        while q:
            u, cur = q.popleft()
            for t, v in g[u]:
                if t >= cur and t < time[v]:
                    time[v] = t
                    q.append((v, t))

        return [i for i in range(n) if time[i] < INF]
