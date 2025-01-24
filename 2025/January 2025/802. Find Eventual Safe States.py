class Solution:
    def dfs(self, node, adj, visit, inStack):
        if inStack[node]: return True
        if visit[node]: return False
        visit[node], inStack[node] = True, True
        if any(self.dfs(neighbor, adj, visit, inStack) for neighbor in adj[node]):
            return True
        inStack[node] = False
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n, visit, inStack = len(graph), [False] * len(graph), [False] * len(graph)
        for i in range(n): self.dfs(i, graph, visit, inStack)
        return [i for i in range(n) if not inStack[i]]
