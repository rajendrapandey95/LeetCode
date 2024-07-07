class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk = numBottles
        
        while numBottles >= numExchange:
            exchanged = numBottles // numExchange
            total_drunk += exchanged
            numBottles = numBottles % numExchange + exchanged

        return total_drunk
