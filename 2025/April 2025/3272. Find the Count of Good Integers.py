from math import factorial
from typing import List

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        unique_sorted_palins = set()
        base = 10 ** ((n - 1) // 2)
        skip_center = n % 2

        for i in range(base, base * 10):
            s = str(i)
            full = s + s[::-1][skip_center:]
            pal_num = int(full)

            if pal_num % k == 0:
                unique_sorted_palins.add(''.join(sorted(full)))

        fact = [factorial(i) for i in range(n + 1)]

        def permutations(counts):
            total = (n - counts[0]) * fact[n - 1]
            for c in counts:
                total //= fact[c]
            return total

        result = 0
        for s in unique_sorted_palins:
            digit_counts = [0] * 10
            for ch in s:
                digit_counts[int(ch)] += 1
            result += permutations(digit_counts)

        return result
