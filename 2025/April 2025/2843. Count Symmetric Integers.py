class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1):
            s = str(num)
            if len(s) % 2 == 0:
                mid = len(s) // 2
                left = sum(int(x) for x in s[:mid])
                right = sum(int(x) for x in s[mid:])
                if left == right:
                    count += 1
        return count
