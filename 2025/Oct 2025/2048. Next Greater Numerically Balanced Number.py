from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        beautiful_nums = []
        from itertools import permutations

        for digits in range(1, 8):
            nums = []

            for comb in permutations('1223334444555556666667777777'[:sum(range(digits+1))], digits):
                s = ''.join(sorted(comb))
                count = Counter(s)
                if all(count[d] == int(d) for d in count):
                    nums.append(int(s))
            beautiful_nums += nums

        beautiful_nums = sorted(set(beautiful_nums))

        for num in beautiful_nums:
            if num > n:
                return num
