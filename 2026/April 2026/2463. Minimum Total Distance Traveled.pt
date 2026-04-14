from typing import List

class Solution:
    def minimumTotalDistance(self, robots: List[int], factories: List[List[int]]) -> int:
        robots.sort()
        factory_positions = [pos for pos, cap in sorted(factories) for _ in range(cap)]
        next_dp, current_dp = [0] * (len(factory_positions) + 1), [0] * (len(factory_positions) + 1)

        for i in range(len(robots) - 1, -1, -1):
            if i != len(robots) - 1:
                next_dp[-1] = float('inf')
            current_dp[-1] = float('inf')
            for j in range(len(factory_positions) - 1, -1, -1):
                assign = abs(robots[i] - factory_positions[j]) + next_dp[j + 1]
                current_dp[j] = min(assign, current_dp[j + 1])
            next_dp = current_dp[:]

        return current_dp[0]
