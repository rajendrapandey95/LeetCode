class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        answer = []
        self.backtrack(candidates, target, 0, [], answer)
        return answer

    def backtrack(self, candidates, target, startIdx, path, answer):
        if target == 0:
            answer.append(path[:])
            return
        for i in range(startIdx, len(candidates)):
            if i > startIdx and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            path.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], i + 1, path, answer)
            path.pop()

