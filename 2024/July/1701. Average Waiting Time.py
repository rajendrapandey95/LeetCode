class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        idle = 0
        wait = 0

        for c in customers:
            idle = max(c[0], idle) + c[1]
            wait += idle - c[0]

        return wait / len(customers)
