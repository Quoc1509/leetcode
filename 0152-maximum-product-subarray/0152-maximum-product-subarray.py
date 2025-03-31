class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = dpMin = dpMax = nums[0]

        for i in range(1, len(nums)):
            new_dpMax = max(dpMax*nums[i], dpMin*nums[i], nums[i])
            dpMin = min(dpMin*nums[i], dpMax*nums[i], nums[i])
            dpMax = new_dpMax
            res = max(dpMax, res)
        return res

        
        