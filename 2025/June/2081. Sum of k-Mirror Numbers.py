class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def pal(x):
            d = []
            while x:
                d.append(x % k)
                x //= k
            return d == d[::-1]

        ans = cnt = 0
        left = 1
        while cnt < n:
            for op in (0, 1):
                for i in range(left, left * 10):
                    if cnt == n: break
                    num, x = i, i//10 if op else i
                    while x:
                        num = num*10 + x % 10
                        x //= 10
                    if pal(num):
                        ans += num
                        cnt += 1
            left *= 10
        return ans
