class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        for start in range(1, 10):
            self._generate(start, n, result)
        return result

    def _generate(self, current: int, limit: int, result: List[int]):
        if current > limit:
            return
        result.append(current)
        for next_digit in range(10):
            next_num = current * 10 + next_digit
            if next_num <= limit:
                self._generate(next_num, limit, result)
            else:
                break
