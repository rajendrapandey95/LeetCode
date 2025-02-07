from collections import defaultdict
from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_count = defaultdict(int)
        ball_color = {}
        result = []

        for ball, color in queries:
            if ball in ball_color:
                prev_color = ball_color[ball]
                color_count[prev_color] -= 1
                if color_count[prev_color] == 0:
                    del color_count[prev_color]

            ball_color[ball] = color
            color_count[color] += 1

            result.append(len(color_count))

        return result
