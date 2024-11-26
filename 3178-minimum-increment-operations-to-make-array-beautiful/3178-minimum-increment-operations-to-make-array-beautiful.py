class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        @cache
        def dp(i, j):
            if i >= len(nums):
                return 0
            increase = inf
            noIncrease = inf
            if i - j < 3:
                noIncrease = dp(i+1, j)
            increase = dp(i+1, i) + max(0, k-nums[i])
            return min(increase, noIncrease)
        ans = dp(0, -1)
        return ans
