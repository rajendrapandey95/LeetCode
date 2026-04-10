class Solution:
    def minimumDistance(self, nums):
        last = {}
        ans = float('inf')

        for i,x in enumerate(nums):
            if x in last and len(last[x])>=2:
                ans = min(ans, i - last[x][0])
                last[x].pop(0)
            last.setdefault(x, []).append(i)

        return -1 if ans==float('inf') else ans*2
