class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        prefix_sum = [0] * (len(words) + 1)

        for i, word in enumerate(words):
            prefix_sum[i + 1] = prefix_sum[i] + (word[0] in vowels and word[-1] in vowels)

        return [prefix_sum[q[1] + 1] - prefix_sum[q[0]] for q in queries]
