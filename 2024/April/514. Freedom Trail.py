class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def distance(p1, p2):
            return min(abs(p1 - p2), len(ring) - abs(p1 - p2))

        positions = {}
        for i, c in enumerate(ring):
            if c not in positions:
                positions[c] = []
            positions[c].append(i)

        dp = [[-1] * len(ring) for _ in range(len(key))]

        def dfs(index, ring_index):
            if index == len(key):
                return 0
            if dp[index][ring_index] != -1:
                return dp[index][ring_index]

            char_positions = positions[key[index]]
            min_steps = float('inf')
            for pos in char_positions:
                steps = distance(ring_index, pos)
                steps += dfs(index + 1, pos)
                min_steps = min(min_steps, steps)

            dp[index][ring_index] = min_steps
            return min_steps

        return len(key) + dfs(0, 0)
