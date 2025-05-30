from typing import List
from collections import deque
from math import inf

class Solution:
    def bfs(self, startNode: int, edges: List[int], dist: List[int]) -> None:
        n = len(edges)
        q = deque([startNode])
        visit = [False] * n
        dist[startNode] = 0

        while q:
            node = q.popleft()

            if visit[node]:
                continue

            visit[node] = True
            neighbor = edges[node]

            if neighbor != -1 and not visit[neighbor]:
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist1 = [inf] * n
        dist2 = [inf] * n

        self.bfs(node1, edges, dist1)
        self.bfs(node2, edges, dist2)

        minDistNode = -1
        minDistTillNow = inf

        for currNode in range(n):
            maxDist = max(dist1[currNode], dist2[currNode])
            if maxDist < minDistTillNow:
                minDistTillNow = maxDist
                minDistNode = currNode

        return minDistNode
