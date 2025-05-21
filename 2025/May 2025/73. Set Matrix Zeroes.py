class Solution(object):
    def setZeroes(self, matrix):
        zeroinFirstCol = False
        zeroinFirstRow = False
        rows = len(matrix)
        cols = len(matrix[0])

        for j in range(cols):
            if matrix[0][j] == 0:
                zeroinFirstRow = True
                break

        for i in range(rows):
            if matrix[i][0] == 0:
                zeroinFirstCol = True
                break

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if zeroinFirstRow:
            for j in range(cols):
                matrix[0][j] = 0

        if zeroinFirstCol:
            for i in range(rows):
                matrix[i][0] = 0
