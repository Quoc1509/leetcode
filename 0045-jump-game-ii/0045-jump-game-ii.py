class Solution:
    def jump(self, nums: List[int]) -> int:
        # if len(nums) == 1: return 0
        dp = [0] * len(nums)
        j = 1
        for i in range(len(nums)):
            while j < min(len(nums), nums[i] + i+1):
                dp[j] = dp[i] + 1
                j += 1
        return dp[-1]