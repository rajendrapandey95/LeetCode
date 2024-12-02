class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words_list = sentence.split()
        for word_index, word in enumerate(words_list):
            if word.startswith(searchWord):
                return word_index + 1
        return -1
