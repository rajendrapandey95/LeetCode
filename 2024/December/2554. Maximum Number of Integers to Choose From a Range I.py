class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)  
        count = 0
        total = 0

        for num in range(1, n + 1):
            if num in banned_set:  
                continue

            if total + num > maxSum:  
                break

            total += num
            count += 1

        return count
