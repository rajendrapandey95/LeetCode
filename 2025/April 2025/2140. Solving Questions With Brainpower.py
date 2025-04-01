from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            next_index = i + brainpower + 1
            dp[i] = points + (dp[next_index] if next_index < n else 0)
            if i < n - 1:
                dp[i] = max(dp[i], dp[i + 1])
        
        return dp[0]
