class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:      
            extra = numBottles % numExchange
            numBottles //= numExchange
            res += numBottles
            numBottles += extra
            
        return res