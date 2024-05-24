class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        W = len(words)
        self.max_score = 0
        freq = [0 for i in range(26)]
        subset_letters = [0 for i in range(26)]
        for c in letters:
            freq[ord(c) - 97] += 1

        def is_valid_word(subset_letters):
            for c in range(26):
                if freq[c] < subset_letters[c]:
                    return False
            else:
                return True
        
        def check(w, words, score, subset_letters, total_score):
            if w == -1:
                self.max_score = max(self.max_score, total_score)
                return
            check(w - 1, words, score, subset_letters, total_score)
            L = len(words[w])
            for i in range(L):
                c = ord(words[w][i]) - 97
                subset_letters[c] += 1
                total_score += score[c]

            if is_valid_word(subset_letters):
                check(w - 1, words, score, subset_letters, total_score)
                
            for i in range(L):
                c = ord(words[w][i]) - 97
                subset_letters[c] -= 1
                total_score -= score[c]

        check(W - 1, words, score, subset_letters, 0)
        return self.max_score
