class Solution:
    def isPrerequisite(self, adjList: dict, visited: List[bool], src: int, target: int) -> bool:
        if src == target:
            return True
        visited[src] = True
        return any(
            not visited[adj] and self.isPrerequisite(adjList, visited, adj, target)
            for adj in adjList.get(src, [])
        )

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = {i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            adjList[u].append(v)
        return [self.isPrerequisite(adjList, [False] * numCourses, u, v) for u, v in queries]
