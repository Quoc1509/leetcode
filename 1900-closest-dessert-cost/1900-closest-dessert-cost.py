class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        res = [inf]

        def backTracking(price, total, index):
            if price == total:
                res[0] = price
                return
            if abs(total - price) < abs(res[0]-total):             
                res[0] = price
            if abs(total - price) == abs(res[0]-total):             
                res[0] = min(price, res[0])
            if index >= len(toppingCosts): return
            for j in range(3):
                backTracking(price+(j*toppingCosts[index]), total, index+1)

        for i in baseCosts:
            backTracking(i, target, 0)
        return res[0]