from typing import List
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create a dictionary to store the graph
        graph = {}
        for flight in flights:
            start, end, price = flight
            if start not in graph:
                graph[start] = []
            graph[start].append((end, price))
        
        # Priority queue to store the tuples (total price, current city, stops)
        pq = [(0, src, 0)]
        
        while pq:
            price, city, stops = heapq.heappop(pq)
            
            # If destination is reached, return price
            if city == dst:
                return price
            
            # If number of stops exceeds k, skip
            if stops > k:
                continue
            
            # Explore neighbors
            if city in graph:
                for neighbor, cost in graph[city]:
                    heapq.heappush(pq, (price + cost, neighbor, stops + 1))
        
        # If destination cannot be reached within k stops
        return -1
