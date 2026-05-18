class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        if n <= 1:
            return 0

        graph = {}
        for i, x in enumerate(arr):
            if x not in graph:
                graph[x] = []
            graph[x].append(i)

        q = [0]
        visited = {0}
        steps = 0

        while q:
            nxt = []

            for i in q:

                if i == n - 1:
                    return steps

                for nei in graph[arr[i]]:
                    if nei not in visited:
                        visited.add(nei)
                        nxt.append(nei)

                graph[arr[i]].clear()

                for nei in (i - 1, i + 1):
                    if 0 <= nei < n and nei not in visited:
                        visited.add(nei)
                        nxt.append(nei)

            q = nxt
            steps += 1

        return -1
