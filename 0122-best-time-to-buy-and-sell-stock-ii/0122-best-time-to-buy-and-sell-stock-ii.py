class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # res = 0
        # mStock = prices[0]
        # for i in prices:
        #     if i < mStock:
        #         mStock = i
        #         continue
        #     res += (i-mStock)
        #     mStock = i
        # return res

        @cache
        def dfs(i, holding):
            if i == len(prices):
                return 0
            if holding:
                sell = dfs(i+1, 0) + prices[i]
                noSell = dfs(i+1, holding) 
                return max(sell, noSell)
            else:
                buy = dfs(i+1, 1) -prices[i]
                noBuy = dfs(i+1, 0)
                return max(buy, noBuy)

        return dfs(0, 0)
