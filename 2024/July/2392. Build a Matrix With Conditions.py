class Solution:
    def buildMatrix(self, k: int, rowConds: List[List[int]], colConds: List[List[int]]) -> List[List[int]]:
        rOrder = self._topoSort(rowConds, k)
        cOrder = self._topoSort(colConds, k)

        if not rOrder or not cOrder:
            return []

        mat = [[0] * k for _ in range(k)]
        rPos = {num: i for i, num in enumerate(rOrder)}
        cPos = {num: i for i, num in enumerate(cOrder)}

        for num in range(1, k + 1):
            if num in rPos and num in cPos:
                mat[rPos[num]][cPos[num]] = num
        return mat

    def _topoSort(self, edges: List[List[int]], n: int) -> List[int]:
        adj = defaultdict(list)
        order, vis, hasCycle = [], [0] * (n + 1), [False]

        for x, y in edges:
            adj[x].append(y)

        for i in range(1, n + 1):
            if vis[i] == 0:
                self._dfs(i, adj, vis, order, hasCycle)
                if hasCycle[0]:
                    return []
        order.reverse()
        return order

    def _dfs(self, node: int, adj: defaultdict, vis: List[int], order: List[int], hasCycle: List[bool]):
        vis[node] = 1
        for neigh in adj[node]:
            if vis[neigh] == 0:
                self._dfs(neigh, adj, vis, order, hasCycle)
                if hasCycle[0]:
                    return
            elif vis[neigh] == 1:
                hasCycle[0] = True
                return
        vis[node] = 2
        order.append(node)
