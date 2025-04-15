class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        index += 1
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        pos2 = [0] * n
        for i, val in enumerate(nums2):
            pos2[val] = i

        reversedIndexMapping = [0] * n
        for i, val in enumerate(nums1):
            reversedIndexMapping[pos2[val]] = i

        tree = FenwickTree(n)
        res = 0

        for value in range(n):
            pos = reversedIndexMapping[value]
            left = tree.query(pos) 
            tree.update(pos, 1)   
            right = (n - 1 - pos) - (value - left)  
            res += left * right   
        return res
