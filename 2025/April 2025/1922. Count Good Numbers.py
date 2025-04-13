class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def mod_pow(x: int, y: int) -> int:
            result = 1
            x %= MOD
            while y:
                if y & 1:
                    result = result * x % MOD
                x = x * x % MOD
                y >>= 1
            return result

        even_pos = (n + 1) // 2 
        odd_pos = n // 2       

        return mod_pow(5, even_pos) * mod_pow(4, odd_pos) % MOD
