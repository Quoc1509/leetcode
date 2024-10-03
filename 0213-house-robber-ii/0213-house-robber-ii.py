class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return nums[0]
        memo = {}
        def backTracking(i, head):
            if head:
                if i == N-1: return 0
            if i >= N: return 0
            if (i, head) in memo: return memo[i, head]

            res = max(backTracking(i+1, head), backTracking(i+2, head)+nums[i])
            memo[i, head] = res
            return memo[i, head]
        return max(backTracking(0, True), backTracking(1, False))
        

