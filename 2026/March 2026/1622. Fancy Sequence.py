class Fancy:

    MOD = 10**9 + 7

    def __init__(self):
        self.arr = []
        self.a = 1
        self.b = 0

    def append(self, val: int) -> None:
        inv = pow(self.a, self.MOD-2, self.MOD)
        self.arr.append((val-self.b) * inv % self.MOD)

    def addAll(self, inc: int) -> None:
        self.b = (self.b + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.a = self.a * m % self.MOD
        self.b = self.b * m % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        return (self.a * self.arr[idx] + self.b) % self.MOD
