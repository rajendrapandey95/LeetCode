class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def sig(x): return ''.join(sorted(str(x)))
        target = sig(n)
        powers = {sig(1 << i) for i in range(31)}
        return target in powers
