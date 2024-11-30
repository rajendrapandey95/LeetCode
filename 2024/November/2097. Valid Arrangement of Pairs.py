from collections import defaultdict, deque
from typing import List

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adjacencyMatrix = defaultdict(deque)
        inDegree, outDegree = defaultdict(int), defaultdict(int)

        for start, end in pairs:
            adjacencyMatrix[start].append(end)
            outDegree[start] += 1
            inDegree[end] += 1

        result = []

        def visit(node):
            while adjacencyMatrix[node]:
                visit(adjacencyMatrix[node].popleft())
            result.append(node)

        startNode = next((node for node in outDegree if outDegree[node] == inDegree[node] + 1), pairs[0][0])
        visit(startNode)
        result.reverse()

        return [[result[i - 1], result[i]] for i in range(1, len(result))]
