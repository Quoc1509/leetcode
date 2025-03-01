class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        res = [0] * len(nums)
        idx = 0
        for i in range(len(nums)):  
            if nums[i] > 0 and i+1 < len(nums) and nums[i] == nums[i+1]:
                res[idx] = nums[i]*2
                nums[i+1] = 0
                idx += 1
            elif nums[i] > 0:
                res[idx] = nums[i]
                idx += 1
        return res