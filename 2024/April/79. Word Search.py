class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        rows, cols = len(board), len(board[0])

        def dfs(row, col, index):
            
            if index == len(word):
                return True

            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[index]:
                return False

            temp, board[row][col] = board[row][col], '#'

            found = (dfs(row + 1, col, index + 1) or
                     dfs(row - 1, col, index + 1) or
                     dfs(row, col + 1, index + 1) or
                     dfs(row, col - 1, index + 1))

            board[row][col] = temp

            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False
