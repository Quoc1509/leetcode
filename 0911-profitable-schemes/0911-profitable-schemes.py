class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        L = len(group)
        if minProfit == 0:
            return L
        N = 10**9 + 7
        memo = [[[-1] * (minProfit+1) for _ in range(n+1)] for _ in range(L+1)]
        def dp(i, p, pro):
            if i >= L:
                return 0
            # print(pro, p, i)
            if memo[i][p][pro] != -1:
                return memo[i][p][pro]
            count = 0
            if p - group[i] >= 0:
                count = dp(i+1, p-group[i], max(0, pro-profit[i])) + (1 if pro-profit[i] <= 0 else 0)
            memo[i][p][pro] =  (count + dp(i+1, p, pro))%N
            return memo[i][p][pro]
        return dp(0, n, minProfit)
            