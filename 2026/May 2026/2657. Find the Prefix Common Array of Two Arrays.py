class Solution:
    def findThePrefixCommonArray(self, A: list, B: list) -> list:
        n = len(A)
        prefix_common_array = [0] * n
        seen = set()
        common_count = 0

        for i in range(n):
            if A[i] in seen:
                common_count += 1
            else:
                seen.add(A[i])
            if B[i] in seen:
                common_count += 1
            else:
                seen.add(B[i])
            prefix_common_array[i] = common_count

        return prefix_common_array
