class Solution:
    def maximumLength(self, s: str) -> int:
        count = {}
        for start in range(len(s)):
            curr_string = []
            for end in range(start, len(s)):
                if not curr_string or curr_string[-1] == s[end]:
                    curr_string.append(s[end])
                    substring = "".join(curr_string)
                    count[substring] = count.get(substring, 0) + 1
                else:
                    break

        ans = max((len(sub) for sub, freq in count.items() if freq >= 3), default=0)
        return ans if ans > 0 else -1
