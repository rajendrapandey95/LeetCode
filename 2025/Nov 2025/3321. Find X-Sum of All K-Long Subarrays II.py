from collections import defaultdict
from sortedcontainers import SortedList

class Helper:
    def __init__(self, x):
        self.x = x
        self.res = 0
        self.large = SortedList()
        self.small = SortedList()
        self.freq = defaultdict(int)

    def insert(self, num):
        f = self.freq[num]
        if f: self._rem((f, num))
        self.freq[num] = f+1
        self._add((f+1, num))

    def remove(self, num):
        f = self.freq[num]
        self._rem((f, num))
        if f > 1: 
            self.freq[num] = f-1
            self._add((f-1, num))
        else:
            del self.freq[num]

    def get(self):
        return self.res

    def _add(self, p):
        if len(self.large) < self.x or p > self.large[0]:
            self.res += p[0]*p[1]
            self.large.add(p)
            if len(self.large) > self.x:
                q = self.large.pop(0)
                self.res -= q[0]*q[1]
                self.small.add(q)
        else:
            self.small.add(p)

    def _rem(self, p):
        if p in self.large:
            self.res -= p[0]*p[1]
            self.large.remove(p)
            if self.small:
                q = self.small.pop()
                self.res += q[0]*q[1]
                self.large.add(q)
        else:
            self.small.remove(p)


class Solution:
    def findXSum(self, nums, k, x):
        H = Helper(x)
        res = []
        for i, v in enumerate(nums):
            H.insert(v)
            if i >= k:   H.remove(nums[i-k])
            if i >= k-1: res.append(H.get())
        return res
