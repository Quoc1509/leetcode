class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        # @cache
        # def dfs(i, transaction, holding):
        #     if i >= N: return 0

        #     if transaction == 0:
        #         return dfs(i+1, 0, holding)
        #     if holding:
        #         sell = dfs(i+1, transaction-1, 0)+prices[i]
        #         noSell = dfs(i+1, transaction, holding)
        #         return max(sell, noSell)
        #     else:
        #         buy = dfs(i+1, transaction, 1) - prices[i]
        #         noBuy = dfs(i+1, transaction, 0)
        #         return max(buy, noBuy)
        # return dfs(0, 2, 0)

        dp = [[[-inf] * 2 for _ in range(3)] for _ in range(N+1)]
        for i in range(3):
            for j in range(2):
                dp[N][i][j] = 0

        for i in range(N-1, -1, -1):
            for trans in range(3):
                for holding in range(2):
                    if trans == 0:
                        dp[i][trans][holding] = dp[i+1][0][holding]
                    else:
                        if holding == 1:
                            dp[i][trans][holding] = max(dp[i+1][trans-1][0] + prices[i], dp[i+1][trans][holding])
                        else:
                            dp[i][trans][holding] = max(dp[i+1][trans][1] - prices[i], dp[i+1][trans][0])
        return dp[0][2][0]
