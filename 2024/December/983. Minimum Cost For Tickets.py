class Solution:
    def __init__(self):
        self.isTravelNeeded = set()

    def solve(self, dp, days, costs, currDay):
        """
        Helper function to calculate the minimum cost for travel.
        Parameters:
            dp (list): Memoization array for minimum cost.
            days (list): List of days on which travel is required.
            costs (list): List of ticket costs for 1-day, 7-day, and 30-day passes.
            currDay (int): Current day being processed.
        Returns:
            int: Minimum cost from the current day onward.
        """
        # If we have iterated over travel days, return 0.
        if currDay > days[-1]:
            return 0

        # If we don't need to travel on this day, move on to the next day.
        if currDay not in self.isTravelNeeded:
            return self.solve(dp, days, costs, currDay + 1)

        # If already calculated, return the stored answer.
        if dp[currDay] != -1:
            return dp[currDay]

        oneDay = costs[0] + self.solve(dp, days, costs, currDay + 1)
        sevenDay = costs[1] + self.solve(dp, days, costs, currDay + 7)
        thirtyDay = costs[2] + self.solve(dp, days, costs, currDay + 30)

        # Store the cost with the minimum of the three options.
        dp[currDay] = min(oneDay, min(sevenDay, thirtyDay))
        return dp[currDay]

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        Calculate the minimum cost to travel on specified days.
        Parameters:
            days (List[int]): List of days on which travel is required.
            costs (List[int]): List of ticket costs for 1-day, 7-day, and 30-day passes.
        Returns:
            int: Minimum cost to travel on all specified days.
        """
        # The last day on which we need to travel.
        lastDay = days[-1]
        dp = [-1] * (lastDay + 1)

        # Mark the days on which we need to travel.
        self.isTravelNeeded = set(days)

        return self.solve(dp, days, costs, 1)
