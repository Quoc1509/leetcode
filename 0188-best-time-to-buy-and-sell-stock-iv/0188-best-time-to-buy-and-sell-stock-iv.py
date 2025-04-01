class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def dfs(i, holding, transaction):
            if i >= len(prices):
                return 0

            if transaction == 0:
                return dfs(i+1, holding, 0)
            else:
                if holding:
                    return max(dfs(i+1, holding, transaction), dfs(i+1, False, transaction-1)+prices[i])
                else:
                    return max(dfs(i+1, holding, transaction), dfs(i+1, True, transaction)-prices[i])
                
        return dfs(0, False, k)