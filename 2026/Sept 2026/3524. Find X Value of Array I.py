class Solution:
    def resultArray(self, A: List[int], k: int) -> List[int]:
        res = freq = [0] * k

        for n in A:
            n %= k
            cur = [0] * k
            cur[n] = 1

            for x, y in enumerate(freq):
                cur[x * n % k] += y

            freq = cur
            for x, y in enumerate(freq):
                res[x] += y

        return res
