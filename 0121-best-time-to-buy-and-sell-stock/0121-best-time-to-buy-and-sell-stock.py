class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = inf
        for num in prices:
            buy = min(buy, num)
            res = max(res, num-buy)
        return res
