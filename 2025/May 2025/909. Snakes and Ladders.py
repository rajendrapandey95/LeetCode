from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        min_rolls = [-1] * (n * n + 1)
        min_rolls[1] = 0
        q = deque([1])

        while q:
            curr = q.popleft()
            for roll in range(1, 7):
                next_pos = curr + roll
                if next_pos > n * n:
                    break

                row = (next_pos - 1) // n
                col = (next_pos - 1) % n
                if row % 2 == 1:
                    col = n - 1 - col
                board_value = board[n - 1 - row][col]

                destination = board_value if board_value != -1 else next_pos

                if destination == n * n:
                    return min_rolls[curr] + 1

                if min_rolls[destination] == -1:
                    min_rolls[destination] = min_rolls[curr] + 1
                    q.append(destination)

        return -1
