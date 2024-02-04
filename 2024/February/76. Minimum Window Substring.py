from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        min_len = float('inf')
        min_window = ""
        required_chars = Counter(t)
        current_window = Counter()

        required_chars_count = len(required_chars)

        while right < len(s):
            current_char = s[right]
            current_window[current_char] += 1

            if current_char in required_chars and current_window[current_char] == required_chars[current_char]:
                required_chars_count -= 1

            while required_chars_count == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]

                left_char = s[left]
                current_window[left_char] -= 1

                if left_char in required_chars and current_window[left_char] < required_chars[left_char]:
                    required_chars_count += 1

                left += 1

            right += 1

        return min_window
