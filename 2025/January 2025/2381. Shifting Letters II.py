class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)
        for start, end, direction in shifts:
            diff[start] += 1 if direction == 1 else -1
            diff[end + 1] -= 1 if direction == 1 else -1
        cumulative_shift = 0
        result = []
        for i, char in enumerate(s):
            cumulative_shift = (cumulative_shift + diff[i]) % 26
            result.append(chr((ord(char) - ord('a') + cumulative_shift) % 26 + ord('a')))
        return ''.join(result)
