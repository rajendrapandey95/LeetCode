class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        ans = min(minutes[i + 1] - minutes[i] for i in range(len(minutes) - 1))
        return min(ans, 1440 + minutes[0] - minutes[-1])
