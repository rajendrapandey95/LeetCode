from math import gcd
from collections import defaultdict

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # Function to check if gcd(nums[i], nums[j]) > 1
        def has_common_divisor(i, j):
            return gcd(nums[i], nums[j]) > 1

        # Build the graph
        graph = defaultdict(list)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if has_common_divisor(i, j):
                    graph[i].append(j)
                    graph[j].append(i)

        # Perform DFS to check reachability between all pairs of indices
        def dfs(node, visited):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

        visited = set()
        dfs(0, visited)

        # Check if all indices are reachable
        return len(visited) == n

# Example usage:
# nums = [2, 3, 4, 5]
# print(Solution().canTraverseAllPairs(nums))
