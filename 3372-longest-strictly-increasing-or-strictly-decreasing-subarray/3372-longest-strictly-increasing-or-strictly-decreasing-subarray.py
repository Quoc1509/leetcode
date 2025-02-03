class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        increase, decrease = 1, 1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                decrease += 1
                increase = 1
            elif nums[i] < nums[i+1]:
                increase += 1
                decrease = 1
            else:
                increase = 1
                decrease = 1
            res = max(res, increase, decrease)
        return res
