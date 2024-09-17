class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> list:
        count = {}

        for word in A.split() + B.split():
            count[word] = count.get(word, 0) + 1

        return [word for word in count if count[word] == 1]
