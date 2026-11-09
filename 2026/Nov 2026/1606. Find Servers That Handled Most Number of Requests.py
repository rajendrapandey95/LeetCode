class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free = list(range(k))  

        handled, busy = [], []  
        for i, (t, d) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= t:  
                heappush(free, i + (heappop(busy)[1] - i) % k)  
            if free:  
                x = heappop(free) % k
                heappush(busy, (t + d, x))
                handled.append(x)

        return multimode(handled)
