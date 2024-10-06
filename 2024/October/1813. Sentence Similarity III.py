class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1_words, s2_words = sentence1.split(), sentence2.split()
        start, ends1, ends2 = 0, len(s1_words) - 1, len(s2_words) - 1

        if len(s1_words) > len(s2_words):
            return self.areSentencesSimilar(sentence2, sentence1)

        while start < len(s1_words) and s1_words[start] == s2_words[start]:
            start += 1

        while ends1 >= 0 and s1_words[ends1] == s2_words[ends2]:
            ends1 -= 1
            ends2 -= 1

        return ends1 < start
