class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res, cur = 0, 0
        for i in range(2, len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                res += cur + 1
                cur += 1
            else:
                cur = 0
        return res