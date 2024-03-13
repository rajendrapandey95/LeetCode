class Solution:
    def pivotInteger(self, n: int) -> int:
        left, right = 1, n
        
        total_sum = n * (n + 1) // 2

        while left < right:
            mid = (left + right) // 2

            if mid * mid - total_sum < 0:
                left = mid + 1  
            else:
                right = mid  

        if left * left - total_sum == 0:
            return left
        else:
            return -1
