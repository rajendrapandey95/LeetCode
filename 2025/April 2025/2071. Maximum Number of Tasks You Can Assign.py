from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        def can_assign(mid):
            w = SortedList(workers[-mid:])
            p = pills
            for i in reversed(range(mid)):
                if w[-1] >= tasks[i]:
                    w.pop()
                else:
                    if not p: return False
                    idx = w.bisect_left(tasks[i] - strength)
                    if idx == len(w): return False
                    w.pop(idx)
                    p -= 1
            return True

        l, r, ans = 1, min(len(tasks), len(workers)), 0
        while l <= r:
            m = (l + r) // 2
            if can_assign(m):
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans
