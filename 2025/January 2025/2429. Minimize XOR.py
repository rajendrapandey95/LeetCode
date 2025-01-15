class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        target_set_bits_count = bin(num2).count("1")
        result = num1
        set_bits_count = bin(result).count("1")

        for bit in range(32):
            if set_bits_count >= target_set_bits_count:
                break
            if not (result & (1 << bit)):
                result |= (1 << bit)
                set_bits_count += 1

        for bit in range(32):
            if set_bits_count <= target_set_bits_count:
                break
            if result & (1 << bit):
                result &= ~(1 << bit)
                set_bits_count -= 1

        return result
