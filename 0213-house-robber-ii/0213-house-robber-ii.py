class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return nums[0]
        @cache
        def backTracking(i, head):
            if head:
                if i == N-1: return 0
            if i >= N: return 0
            # if i in memo: return memo[i]

            res = max(backTracking(i+1, head), backTracking(i+2, head)+nums[i])
            # memo[i] = res
            return res
        return max(backTracking(0, True), backTracking(1, False))
        

