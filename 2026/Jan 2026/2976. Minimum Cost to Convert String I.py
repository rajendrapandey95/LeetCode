from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        min_cost = [[float('inf')] * 26 for _ in range(26)]
        for o, c, co in zip(original, changed, cost):
            min_cost[ord(o) - ord('a')][ord(c) - ord('a')] = min(min_cost[ord(o) - ord('a')][ord(c) - ord('a')], co)
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    min_cost[i][j] = min(min_cost[i][j], min_cost[i][k] + min_cost[k][j])
        total_cost = 0
        for s, t in zip(source, target):
            if s != t:
                s_idx, t_idx = ord(s) - ord('a'), ord(t) - ord('a')
                if min_cost[s_idx][t_idx] == float('inf'):
                    return -1
                total_cost += min_cost[s_idx][t_idx]
        return total_cost
