import heapq

class Solution:
    MOD = 10**9 + 7

    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        graph = [[] for _ in range(n)]
        for start_node, end_node, travel_time in roads:
            graph[start_node].append((end_node, travel_time))
            graph[end_node].append((start_node, travel_time))

        min_heap = [(0, 0)] 

        shortest_time = [float("inf")] * n

        path_count = [0] * n

        shortest_time[0] = 0  
        path_count[0] = 1     

        while min_heap:
            curr_time, curr_node = heapq.heappop(min_heap)

            if curr_time > shortest_time[curr_node]:
                continue

            for neighbor_node, road_time in graph[curr_node]:
                new_time = curr_time + road_time

                if new_time < shortest_time[neighbor_node]:
                    shortest_time[neighbor_node] = new_time
                    path_count[neighbor_node] = path_count[curr_node]
                    heapq.heappush(min_heap, (new_time, neighbor_node))

                elif new_time == shortest_time[neighbor_node]:
                    path_count[neighbor_node] = (path_count[neighbor_node] + path_count[curr_node]) % self.MOD

        return path_count[n - 1]
