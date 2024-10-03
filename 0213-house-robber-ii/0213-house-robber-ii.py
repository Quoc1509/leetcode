class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return nums[0]
        # memo = {}
        # def backTracking(i, head):
        #     if head:
        #         if i == N-1: return 0
        #     if i >= N: return 0
        #     if (i, head) in memo: return memo[i, head]

        #     res = max(backTracking(i+1, head), backTracking(i+2, head)+nums[i])
        #     memo[i, head] = res
        #     return memo[i, head]
        # return max(backTracking(0, True), backTracking(1, False))

        dp = [[0] * 2 for _ in range(N+2)]
        

        for i in range(N-1, -1, -1):
            for head in range(2):
                if head and i == N-1:
                    continue
                dp[i][head] = max(dp[i+1][head], dp[i+2][head]+nums[i])

        return max(dp[0][1], dp[1][0])

        
        

