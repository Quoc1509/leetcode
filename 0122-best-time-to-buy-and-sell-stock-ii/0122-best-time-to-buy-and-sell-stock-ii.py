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

        #top-down
        # @cache
        # def dfs(i, holding):
        #     if i == len(prices):
        #         return 0
        #     if holding:
        #         sell = dfs(i+1, 0) + prices[i]
        #         noSell = dfs(i+1, holding) 
        #         return max(sell, noSell)
        #     else:
        #         buy = dfs(i+1, 1) -prices[i]
        #         noBuy = dfs(i+1, 0)
        #         return max(buy, noBuy)

        # return dfs(0, 0)

        #bottom-up
        N = len(prices)
        dp = [[-inf] * 2 for _ in range(N+1)]
        for i in range(2):
            dp[N][i] = 0 

        for i in range(N-1, -1, -1):
            for holding in range(2):
                if holding:
                    dp[i][holding] = max(dp[i+1][0] + prices[i], dp[i+1][holding])
                else:
                    dp[i][holding] = max(dp[i+1][1] - prices[i], dp[i+1][holding])

        return dp[0][0]
                
