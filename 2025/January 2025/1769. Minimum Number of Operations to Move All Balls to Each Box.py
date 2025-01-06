class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        return [sum(abs(i - j) for j, b in enumerate(boxes) if b == "1") for i in range(len(boxes))]
