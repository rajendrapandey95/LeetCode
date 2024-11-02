class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        last = words[-1][-1]

        for word in words:
            if word[0] != last:
                return False
            last = word[-1]

        return True
