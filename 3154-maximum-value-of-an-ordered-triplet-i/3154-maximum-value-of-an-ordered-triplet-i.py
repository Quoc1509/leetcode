class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        
        res = 0
        numij, numi = 0, 0
        for k in range(len(nums)):
            res = max(res, numij*nums[k])
            numij = max(numij, numi-nums[k])
            
            if nums[k] > numi:
                numi = nums[k]
        return res

            
            