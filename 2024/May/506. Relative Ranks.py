class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_dict = {score[i]: i for i in range(len(score))}
        sorted_scores = sorted(score, reverse=True)
        answer = [""] * len(score)
        for i in range(len(sorted_scores)):
            if i == 0:
                answer[score_dict[sorted_scores[i]]] = "Gold Medal"
            elif i == 1:
                answer[score_dict[sorted_scores[i]]] = "Silver Medal"
            elif i == 2:
                answer[score_dict[sorted_scores[i]]] = "Bronze Medal"
            else:
                answer[score_dict[sorted_scores[i]]] = str(i + 1)
        return answer
