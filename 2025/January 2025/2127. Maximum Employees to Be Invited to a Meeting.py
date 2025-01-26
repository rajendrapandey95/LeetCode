class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        def _bfs(start: int, visited: set, rev_graph: List[List[int]]) -> int:
            queue = deque([(start, 0)])
            max_dist = 0
            while queue:
                node, dist = queue.popleft()
                for nei in rev_graph[node]:
                    if nei in visited:
                        continue
                    visited.add(nei)
                    queue.append((nei, dist + 1))
                    max_dist = max(max_dist, dist + 1)
            return max_dist

        n = len(favorite)
        rev_graph = [[] for _ in range(n)]
        for p in range(n):
            rev_graph[favorite[p]].append(p)

        longest_cycle, two_cycle_inv = 0, 0
        visited = [False] * n

        for p in range(n):
            if not visited[p]:
                seen, curr, dist = {}, p, 0
                while True:
                    if visited[curr]:
                        break
                    visited[curr] = True
                    seen[curr] = dist
                    dist += 1
                    nxt = favorite[curr]
                    if nxt in seen:
                        cycle_len = dist - seen[nxt]
                        longest_cycle = max(longest_cycle, cycle_len)
                        if cycle_len == 2:
                            nodes = {curr, nxt}
                            two_cycle_inv += 2 + _bfs(nxt, nodes, rev_graph) + _bfs(curr, nodes, rev_graph)
                        break
                    curr = nxt

        return max(longest_cycle, two_cycle_inv)
