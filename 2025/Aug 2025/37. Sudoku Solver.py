class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        N = 9
        rows, cols, boxes = [set() for _ in range(N)], [set() for _ in range(N)], [set() for _ in range(N)]
        empties = []

        for i in range(N):
            for j in range(N):
                if board[i][j] == '.':
                    empties.append((i, j))
                else:
                    d = board[i][j]
                    rows[i].add(d)
                    cols[j].add(d)
                    boxes[(i // 3) * 3 + j // 3].add(d)

        def backtrack(k: int) -> bool:
            if k == len(empties): 
                return True
            i, j = empties[k]
            b = (i // 3) * 3 + j // 3
            for d in map(str, range(1, 10)):
                if d not in rows[i] and d not in cols[j] and d not in boxes[b]:
                    board[i][j] = d
                    rows[i].add(d); cols[j].add(d); boxes[b].add(d)
                    if backtrack(k + 1): 
                        return True
                    board[i][j] = '.'
                    rows[i].remove(d); cols[j].remove(d); boxes[b].remove(d)
            return False

        backtrack(0)
