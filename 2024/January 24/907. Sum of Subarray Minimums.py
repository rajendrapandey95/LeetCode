from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        stack = []
        result = 0

        left = [0] * len(arr)
        right = [0] * len(arr)

        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []

        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            right[i] = stack[-1] if stack else len(arr)
            stack.append(i)

        for i in range(len(arr)):
            result += arr[i] * (i - left[i]) * (right[i] - i)
            result %= mod

        return result
