class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0] * (len(arr) + 1)
        for i in range(1, len(arr) + 1):
            prefix_xor[i] = prefix_xor[i - 1] ^ arr[i - 1]

        result = []
        for q in queries:
            result.append(prefix_xor[q[1] + 1] ^ prefix_xor[q[0]])
        
        return result
