class Solution(object):
    def minCost(self, colors, neededTime):
        ans = cur = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                ans += min(neededTime[i], neededTime[i-1+cur])
                neededTime[i] = max(neededTime[i], neededTime[i-1])
                cur += 1
            else:
                cur = 0
        return ans
