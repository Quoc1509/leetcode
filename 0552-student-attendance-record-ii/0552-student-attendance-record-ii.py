class Solution:
    def checkRecord(self, n: int) -> int:
        N = 10**9+7
        memo = [[[-1] * 3 for _ in range(2)] for _ in range(n+1)]
        def dp(i, p, l):
            if p > 1:
                return 0
            if l >= 3:
                return 0
            if i >= n:
                return 1
            if memo[i][p][l] != -1:
                return memo[i][p][l]
            memo[i][p][l] = (dp(i+1, p, 0) + dp(i+1, p+1, 0) + dp(i+1, p, l+1))%N
            return memo[i][p][l]

        return dp(0, 0, 0)