from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(1, 10 - length + 1):
                num = int("".join(str(start + i) for i in range(length)))
                if low <= num <= high:
                    result.append(num)
        return result
