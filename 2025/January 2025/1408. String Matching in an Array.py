class Solution:
    def stringMatching(self, words):
        return [w for i, w in enumerate(words) if any(w in other for j, other in enumerate(words) if i != j)]
