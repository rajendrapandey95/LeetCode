class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        self.count = 0

        def dfs(node: int, parent: int) -> int:
            subtotal = values[node]

            for nei in adj[node]:
                if nei == parent:
                    continue

                subtotal += dfs(nei, node)
                subtotal %= k

            if subtotal % k == 0:
                self.count += 1
                return 0     

            return subtotal

        dfs(0, -1)
        return self.count
