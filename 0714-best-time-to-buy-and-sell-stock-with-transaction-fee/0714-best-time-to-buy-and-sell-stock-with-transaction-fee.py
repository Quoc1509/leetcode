class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dfs(i, holding):

            if i == len(prices):
                return 0
            
            if holding:
                sell = dfs(i+1, 0) + prices[i] - fee
                noSell = dfs(i+1, 1)
                return max(sell, noSell)
            else:
                buy = dfs(i+1, 1) - prices[i]
                noBuy = dfs(i+1, 0)
                return max(buy, noBuy)
        return dfs(0, 0) 