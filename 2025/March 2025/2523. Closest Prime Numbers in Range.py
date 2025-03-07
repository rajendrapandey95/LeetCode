from typing import List, Tuple

class Solution:
    def _sieve(self, upper_limit: int) -> List[bool]:
        sieve = [True] * (upper_limit + 1)
        sieve[0] = sieve[1] = False  

        for number in range(2, int(upper_limit ** 0.5) + 1):
            if sieve[number]:  
                for multiple in range(number * number, upper_limit + 1, number):
                    sieve[multiple] = False
        return sieve

    def closestPrimes(self, left: int, right: int) -> Tuple[int, int]:
        if right < 2:
            return -1, -1 

        is_prime = self._sieve(right)

        primes = [num for num in range(left, right + 1) if is_prime[num]]

        if len(primes) < 2:
            return -1, -1

        min_diff = float("inf")
        closest_pair = (-1, -1)

        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < min_diff:
                min_diff = diff
                closest_pair = (primes[i - 1], primes[i])

        return closest_pair
