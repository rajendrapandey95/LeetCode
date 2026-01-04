from typing import List
import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        MAXN = 100000
        N = 316

        isPrime = [True] * (N + 1)
        isPrime[0] = isPrime[1] = False
        primes = []

        for i in range(2, N + 1):
            if isPrime[i]:
                primes.append(i)
                for j in range(i * i, N + 1, i):
                    isPrime[j] = False

        div4 = [-1] * (MAXN + 1)
        div4[0] = div4[1] = 0

        def sum4Div(x: int) -> int:
            if div4[x] != -1:
                return div4[x]

            y = x
            total = 1 + x
            cntPF = 0
            xsqrt = int(math.sqrt(x))

            for p in primes:
                if p > xsqrt:
                    break
                if y % p != 0:
                    continue

                e = 0
                while y % p == 0:
                    y //= p
                    e += 1
                cntPF += 1

                if e == 3 and y == 1 and cntPF == 1:
                    div4[x] = 1 + p + p*p + p*p*p
                    return div4[x]

                if e > 1 or cntPF > 2:
                    div4[x] = 0
                    return 0

                total += p

            if y > 1:
                cntPF += 1
                total += y

            div4[x] = total if cntPF == 2 else 0
            return div4[x]

        ans = 0
        for x in nums:
            ans += sum4Div(x)

        return ans
