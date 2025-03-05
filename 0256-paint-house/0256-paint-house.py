class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        @cache
        def dp(n, pre):
            if n >= len(costs):
                return 0
            res = inf
            for i in range(3):
                if i == pre:
                    continue
                res = min(res, dp(n+1, i)+costs[n][i])
            return res
        return dp(0, -1)