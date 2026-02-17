class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for h in range(12):
            bh = h.bit_count()
            for m in range(60):
                if bh + m.bit_count() == turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res
