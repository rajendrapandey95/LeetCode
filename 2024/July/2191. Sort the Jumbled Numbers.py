class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def get_mapped_value(num):
            if num == 0:
                return mapping[0]
            mapped_value = 0
            place = 1
            while num > 0:
                mapped_value += mapping[num % 10] * place
                num //= 10
                place *= 10
            return mapped_value

        pairs = [(get_mapped_value(num), idx) for idx, num in enumerate(nums)]
        pairs.sort()
        return [nums[idx] for _, idx in pairs]
