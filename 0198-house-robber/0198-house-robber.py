class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        # memo = {}
        # def backTracking(i):
            
        #     if i >= N: return 0
        #     if i in memo: return memo[i]
        #     res =  max(backTracking(i+1), backTracking(i+2)+nums[i])
        #     memo[i] = res
        #     return memo[i]
        # return backTracking(0)

        # dp = [0] * (N+2)
        # for i in range(N-1, -1, -1):
        #     dp[i] = max(dp[i+1], dp[i+2]+nums[i])
        # return dp[0]
        # @cache
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     return max(dfs(i+1), dfs(i+2)+nums[i])
        # return dfs(0)

        if len(nums)==1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        dp = [0] * (N)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, N):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]