from collections import defaultdict
from heapq import heappush, heappop
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        max_prob = [0.0] * n
        max_prob[start] = 1.0
        
        pq = [(-1.0, start)] 
        
        while pq:
            prob, node = heappop(pq)
            prob = -prob
            
            if node == end:
                return prob
            
            for neighbor, path_prob in graph[node]:
                new_prob = prob * path_prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heappush(pq, (-new_prob, neighbor))
        
        return 0.0 
