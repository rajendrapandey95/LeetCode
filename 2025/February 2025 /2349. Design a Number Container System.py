from sortedcontainers import SortedSet
from collections import defaultdict

class NumberContainers:

    def __init__(self):
        self.num_to_indices = defaultdict(SortedSet) 
        self.idx_to_num = {}  

    def change(self, index: int, number: int) -> None:
        if index in self.idx_to_num:
            prev_num = self.idx_to_num[index]
            self.num_to_indices[prev_num].remove(index)
            if not self.num_to_indices[prev_num]:
                del self.num_to_indices[prev_num]

        self.idx_to_num[index] = number
        self.num_to_indices[number].add(index)

    def find(self, number: int) -> int:
        return next(iter(self.num_to_indices[number]), -1)
