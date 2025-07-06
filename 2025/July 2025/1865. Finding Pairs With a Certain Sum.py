from collections import Counter

class FindSumPairs:
    def __init__(self, nums1: list[int], nums2: list[int]):
        self.a, self.b = nums1, nums2
        self.c = Counter(nums2)

    def add(self, i: int, val: int) -> None:
        self.c[self.b[i]] -= 1
        self.b[i] += val
        self.c[self.b[i]] += 1

    def count(self, tot: int) -> int:
        return sum(self.c[tot - x] for x in self.a)
