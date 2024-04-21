from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = [False] * n
        
        def dfs(node):
            if node == destination:
                return True
            visited[node] = True
            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
            return False
        
        return dfs(source)
