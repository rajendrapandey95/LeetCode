class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n < 2:
            return 1

        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        queue = deque(node for node, neighbors in graph.items() if len(neighbors) == 1)
        component_count = 0

        while queue:
            current = queue.popleft()
            neighbor = next(iter(graph[current]), -1)

            if neighbor >= 0:
                graph[neighbor].remove(current)

            if values[current] % k == 0:
                component_count += 1
            else:
                values[neighbor] += values[current]

            if neighbor >= 0 and len(graph[neighbor]) == 1:
                queue.append(neighbor)

        return component_count
