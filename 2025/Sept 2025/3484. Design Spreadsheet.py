class Spreadsheet:
    def __init__(self, n: int):
        self.mpp = {}  

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        for i in range(len(formula)):
            if formula[i] == '+':
                s1, s2 = formula[:i], formula[i + 1:]
                left = self.mpp.get(s1, 0) if s1[0].isalpha() else int(s1)
                right = self.mpp.get(s2, 0) if s2[0].isalpha() else int(s2)
                return left + right
        return 0

    def setCell(self, cell: str, val: int) -> None:
        self.mpp[cell] = val

    def resetCell(self, cell: str) -> None:
        if cell in self.mpp:
            del self.mpp[cell]
