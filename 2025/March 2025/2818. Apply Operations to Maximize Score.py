from typing import List
from collections import deque

class Solution:
    MOD = int(1e9 + 7)

    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prime_scores = [0] * n

        max_element = max(nums)

        primes = self.get_primes(max_element)

        for index in range(n):
            num = nums[index]

            for prime in primes:
                if prime * prime > num:
                    break  
                if num % prime != 0:
                    continue  

                prime_scores[index] += 1  
                while num % prime == 0:
                    num //= prime  

            if num > 1:
                prime_scores[index] += 1

        next_dominant = [n] * n
        prev_dominant = [-1] * n

        decreasing_prime_score_stack = deque()

        for index in range(n):
            while (
                decreasing_prime_score_stack
                and prime_scores[decreasing_prime_score_stack[-1]] < prime_scores[index]
            ):
                top_index = decreasing_prime_score_stack.pop()
                next_dominant[top_index] = index  

            if decreasing_prime_score_stack:
                prev_dominant[index] = decreasing_prime_score_stack[-1]  

            decreasing_prime_score_stack.append(index)

        num_of_subarrays = [
            (next_dominant[i] - i) * (i - prev_dominant[i]) for i in range(n)
        ]

        sorted_array = sorted(enumerate(nums), key=lambda x: -x[1])

        score = 1 

        def _power(base, exponent):
            res = 1
            while exponent > 0:
                if exponent % 2:
                    res = (res * base) % self.MOD
                base = (base * base) % self.MOD
                exponent //= 2
            return res

        processing_index = 0

        while k > 0:
            index, num = sorted_array[processing_index]
            processing_index += 1

            operations = min(k, num_of_subarrays[index])

            score = (score * _power(num, operations)) % self.MOD

            k -= operations

        return score

    def get_primes(self, limit: int) -> List[int]:
        is_prime = [True] * (limit + 1)
        primes = []

        for number in range(2, limit + 1):
            if is_prime[number]:
                primes.append(number)
                for multiple in range(number * number, limit + 1, number):
                    is_prime[multiple] = False

        return primes
