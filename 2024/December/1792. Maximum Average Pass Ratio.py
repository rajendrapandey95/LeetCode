import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
       
        def gain(p, t): return (p + 1) / (t + 1) - p / t

        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            heapq.heappush(heap, (-gain(p + 1, t + 1), p + 1, t + 1))

        return sum(p / t for _, p, t in heap) / len(classes)
