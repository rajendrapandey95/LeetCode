from typing import List
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create a dictionary to store the graph
        graph_out = {}
        graph_in = {}
        for flight in flights:
            start, end, price = flight
            if start not in graph_out:
                graph_out[start] = []
            if end not in graph_in:
                graph_in[end] = []
            graph_out[start].append((end, price))
            graph_in[end].append((start, price))
        
        # Priority queues to store the tuples (total price, current city, stops)
        pq_out = [(0, src, 0)]
        pq_in = [(0, dst, 0)]
        
        # Dictionaries to keep track of visited nodes and their costs
        visited_out = {}
        visited_in = {}
        
        while pq_out or pq_in:
            # Search from source
            if pq_out:
                price, city, stops = heapq.heappop(pq_out)
                if city == dst:  # If destination is reached
                    return price
                if city not in visited_out or stops <= visited_out[city]:
                    visited_out[city] = stops
                    if stops <= k:
                        if city in graph_out:
                            for neighbor, cost in graph_out[city]:
                                heapq.heappush(pq_out, (price + cost, neighbor, stops + 1))
            
            # Search from destination
            if pq_in:
                price, city, stops = heapq.heappop(pq_in)
                if city == src:  # If destination is reached
                    return price
                if city not in visited_in or stops <= visited_in[city]:
                    visited_in[city] = stops
                    if stops <= k:
                        if city in graph_in:
                            for neighbor, cost in graph_in[city]:
                                heapq.heappush(pq_in, (price + cost, neighbor, stops + 1))
        
        # If destination cannot be reached within k stops
        return -1
