class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        @cache
        def backTracking(i):

            if i >= N: return 0

            return max(backTracking(i+1), backTracking(i+2)+nums[i])

        return backTracking(0)