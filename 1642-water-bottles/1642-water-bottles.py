class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:      
            res += numBottles // numExchange
            extra = numBottles % numExchange
            numBottles //= numExchange
            numBottles += extra
            print(numBottles)
        return res