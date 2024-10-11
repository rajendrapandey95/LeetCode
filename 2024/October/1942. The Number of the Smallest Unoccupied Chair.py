class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target_time = times[targetFriend]
        times.sort()
        n = len(times)
        chair_time = [0] * n

        for start, end in times:
            for i in range(n):
                if chair_time[i] <= start:
                    chair_time[i] = end
                    if [start, end] == target_time:
                        return i
        return 0
