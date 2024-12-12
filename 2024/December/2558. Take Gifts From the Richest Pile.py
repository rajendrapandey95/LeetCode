import math

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        gifts.sort()

        for _ in range(k):
            max_element = gifts.pop()
            sqrt_value = math.floor(math.sqrt(max_element))
            gifts.insert(next((i for i, x in enumerate(gifts) if x > sqrt_value), len(gifts)), sqrt_value)

        return sum(gifts)
