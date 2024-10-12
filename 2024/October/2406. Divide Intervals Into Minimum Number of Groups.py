class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = [(i[0], 1) for i in intervals] + [(i[1] + 1, -1) for i in intervals]
        events.sort()

        cur, max_int = 0, 0
        for _, e in events:
            cur += e
            max_int = max(max_int, cur)

        return max_int
