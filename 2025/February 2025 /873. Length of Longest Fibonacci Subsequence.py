class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        num_set, max_len, n = set(arr), 0, len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                a, b, length = arr[j], arr[i] + arr[j], 2
                while b in num_set:
                    a, b, length = b, a + b, length + 1
                    max_len = max(max_len, length)
        return max_len
