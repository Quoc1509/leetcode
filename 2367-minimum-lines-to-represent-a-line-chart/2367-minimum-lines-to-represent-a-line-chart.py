class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) <= 1: return 0
        stockPrices.sort()
        def line(x1, x2, y1, y2):
            a, b = (y2-y1), (x2-x1)
            g = gcd(a, b)
            a //= g
            b //= g
            return a, b
            
        x, y = line(stockPrices[0][0], stockPrices[1][0], stockPrices[0][1], stockPrices[1][1])
        res = 1
        for i in range(1, len(stockPrices)-1):
            c, d = line(stockPrices[i][0], stockPrices[i+1][0], stockPrices[i][1], stockPrices[i+1][1])
            if x != c or y != d:
                res += 1
                x, y = c, d
                
        return res