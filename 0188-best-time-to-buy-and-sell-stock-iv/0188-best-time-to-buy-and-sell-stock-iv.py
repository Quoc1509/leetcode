class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)

        @cache
        def dfs(i, transaction, holding):
            if i >= N: return 0

            if transaction == 0: 
                return dfs(i+1, 0, holding)
            if holding:
                sell = dfs(i+1, transaction-1, 0) + prices[i]
                noSell = dfs(i+1, transaction, holding)
                return max(sell, noSell)
            else:
                buy = dfs(i+1, transaction, 1) - prices[i]
                noBuy = dfs(i+1, transaction, 0)
                return max(buy, noBuy)
        return dfs(0, k, 0)