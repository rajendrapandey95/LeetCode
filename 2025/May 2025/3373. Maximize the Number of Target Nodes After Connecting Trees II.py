from typing import List

class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> List[int]:

        def dfs(node: int, parent: int, depth: int, children: List[List[int]], color: List[int]) -> int:
            color[node] = depth % 2
            count = 1 - color[node]  # 1 if even, 0 if odd
            for child in children[node]:
                if child != parent:
                    count += dfs(child, node, depth + 1, children, color)
            return count

        def build(edges: List[List[int]], color: List[int]) -> List[int]:
            n = len(edges) + 1
            children = [[] for _ in range(n)]
            for u, v in edges:
                children[u].append(v)
                children[v].append(u)
            even_count = dfs(0, -1, 0, children, color)
            odd_count = n - even_count
            return [even_count, odd_count]

        n = len(edges1) + 1
        m = len(edges2) + 1
        color1 = [0] * n
        color2 = [0] * m

        count1 = build(edges1, color1)
        count2 = build(edges2, color2)

        max_count2 = max(count2)
        result = [count1[color1[i]] + max_count2 for i in range(n)]

        return result
