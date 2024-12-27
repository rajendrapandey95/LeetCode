class Solution:
    def maxScoreSightseeingPair(self, values):
        max_left, max_score = values[0], 0
        for i in range(1, len(values)):
            max_score = max(max_score, max_left + values[i] - i)
            max_left = max(max_left, values[i] + i)
        return max_score
