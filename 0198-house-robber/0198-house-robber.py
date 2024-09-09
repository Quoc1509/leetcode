class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        memo = {}
        def backTracking(i):

            if i >= N: return 0
            if i in memo: return memo[i]
            res =  max(backTracking(i+1), backTracking(i+2)+nums[i])
            memo[i] = res
            return memo[i]
        return backTracking(0)