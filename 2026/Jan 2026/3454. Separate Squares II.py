class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        tot = sum(l*l for _, y, l in squares)
        hi = max(y + l for _, y, l in squares)

        def ok(Y):
            return sum(l * min(max(Y - y, 0), l) for _, y, l in squares) * 2 >= tot

        lo = 0.0
        while hi - lo > 1e-5:
            mid = (lo + hi) / 2
            if ok(mid): hi = mid
            else: lo = mid
        return hi
