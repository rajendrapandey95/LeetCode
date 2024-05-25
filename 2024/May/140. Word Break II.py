class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memoization = {}
        return self._dfs(s, word_set, memoization)

    def _dfs(self, remaining_str: str, word_set: set, memoization: dict) -> List[str]:
        if remaining_str in memoization:
            return memoization[remaining_str]
        if not remaining_str:
            return [""]
        results = []
        for i in range(1, len(remaining_str) + 1):
            current_word = remaining_str[:i]
            if current_word in word_set:
                for next_word in self._dfs(remaining_str[i:], word_set, memoization):
                    results.append(current_word + (" " if next_word else "") + next_word)
        memoization[remaining_str] = results
        return results
