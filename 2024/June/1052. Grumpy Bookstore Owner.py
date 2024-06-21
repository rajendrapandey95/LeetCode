class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        unrealized_customers = 0

        for i in range(minutes):
            unrealized_customers += customers[i] * grumpy[i]

        max_unrealized_customers = unrealized_customers

        for i in range(minutes, n):
            unrealized_customers += customers[i] * grumpy[i]
            unrealized_customers -= customers[i - minutes] * grumpy[i - minutes]
            max_unrealized_customers = max(max_unrealized_customers, unrealized_customers)

        total_customers = max_unrealized_customers

        for i in range(n):
            total_customers += customers[i] * (1 - grumpy[i])

        return total_customers
