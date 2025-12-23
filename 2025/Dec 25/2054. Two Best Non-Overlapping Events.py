from bisect import bisect_right

class Solution:
    def maxTwoEvents(self, events):
        events.sort()
        n = len(events)

        # suffix max of values
        suf = [0]*(n+1)
        for i in range(n-1, -1, -1):
            suf[i] = max(suf[i+1], events[i][2])

        ans = 0
        for i, (s, e, v) in enumerate(events):
            j = bisect_right(events, e, key=lambda x: x[0])
            ans = max(ans, v + suf[j])

        return ans
