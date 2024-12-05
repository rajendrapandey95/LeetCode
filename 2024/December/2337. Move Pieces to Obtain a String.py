class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_queue = [(char, i) for i, char in enumerate(start) if char != "_"]
        target_queue = [(char, i) for i, char in enumerate(target) if char != "_"]

        if len(start_queue) != len(target_queue):
            return False

        for (s_char, s_index), (t_char, t_index) in zip(start_queue, target_queue):
            if s_char != t_char or (s_char == "L" and s_index < t_index) or (s_char == "R" and s_index > t_index):
                return False

        return True
