class Solution:
    def getAncestors(self, num_nodes: int, edges: List[List[int]]) -> List[List[int]]:
        adjacency_list = [[] for _ in range(num_nodes)]

        for edge in edges:
            parent, child = edge
            adjacency_list[child].append(parent)

        all_ancestors = []

        for node in range(num_nodes):
            ancestors = []
            visited = set()
            self.dfs(node, adjacency_list, visited)
            for ancestor in range(num_nodes):
                if ancestor == node:
                    continue
                if ancestor in visited:
                    ancestors.append(ancestor)
            all_ancestors.append(ancestors)

        return all_ancestors

    def dfs(self, current_node: int, adjacency_list: List[List[int]], visited: set):
        visited.add(current_node)

        for parent in adjacency_list[current_node]:
            if parent not in visited:
                self.dfs(parent, adjacency_list, visited)
