class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5: return 0
        nums.sort()
        res = inf
        for i in range(4):
            temp = nums[-1-i] - nums[3-i]
            res = min(res, temp)
        return res
