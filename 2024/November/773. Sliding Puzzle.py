from typing import List
from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start_state = "".join(str(num) for row in board for num in row)
        target_state = "123450"
        directions = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [3, 5, 1],
            [4, 2],
        ]

        def swap(state, i, j):
            state = list(state)
            state[i], state[j] = state[j], state[i]
            return "".join(state)

        queue = deque([(start_state, start_state.index("0"), 0)])
        visited = set()
        visited.add(start_state)

        while queue:
            current_state, zero_pos, moves = queue.popleft()
            if current_state == target_state:
                return moves
            for next_pos in directions[zero_pos]:
                new_state = swap(current_state, zero_pos, next_pos)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, next_pos, moves + 1))
        return -1
