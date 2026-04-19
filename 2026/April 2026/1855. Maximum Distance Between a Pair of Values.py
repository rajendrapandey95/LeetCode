class Solution:
    def maxDistance(self, A, B):
        i = j = 0
        while i < len(A) and j < len(B):
            if A[i] > B[j]:
                i += 1
            j += 1
        return j - i - 1
