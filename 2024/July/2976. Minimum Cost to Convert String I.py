from typing import List
import heapq

class Solution:
    def minCost(self, src: str, tgt: str, org: List[str], chg: List[str], cst: List[int]) -> int:
        adj = [[] for _ in range(26)]

        for o, ch, cs in zip(org, chg, cst):
            adj[ord(o) - ord("a")].append((ord(ch) - ord("a"), cs))

        min_costs = [self.dijkstra(i, adj) for i in range(26)]

        total_cost = 0
        for s, t in zip(src, tgt):
            if s != t:
                conv_cost = min_costs[ord(s) - ord("a")][ord(t) - ord("a")]
                if conv_cost == float("inf"):
                    return -1
                total_cost += conv_cost

        return total_cost

    def dijkstra(self, start: int, adj: List[List[tuple]]) -> List[int]:
        pq = [(0, start)]
        min_costs = [float("inf")] * 26

        while pq:
            cur_cost, cur = heapq.heappop(pq)
            if min_costs[cur] != float("inf"):
                continue
            min_costs[cur] = cur_cost
            for nxt, nxt_cost in adj[cur]:
                if min_costs[nxt] == float("inf"):
                    heapq.heappush(pq, (cur_cost + nxt_cost, nxt))

        return min_costs
