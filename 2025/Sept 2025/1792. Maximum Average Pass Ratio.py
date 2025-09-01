import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p, t): return (p+1)/(t+1) - p/t
        pq=[(-gain(p,t),p,t) for p,t in classes]
        heapq.heapify(pq)
        for _ in range(extraStudents):
            g,p,t=heapq.heappop(pq)
            p,t=p+1,t+1
            heapq.heappush(pq,(-gain(p,t),p,t))
        return sum(p/t for _,p,t in pq)/len(pq)
