class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0:
            A = int(a[i]) if i >= 0 else 0
            B = int(b[j]) if j >= 0 else 0

            res.append(str((A ^ B) ^ carry))
            carry = (A & B) | ((A ^ B) & carry)

            i -= 1
            j -= 1

        if carry:
            res.append("1")

        return "".join(res[::-1])
