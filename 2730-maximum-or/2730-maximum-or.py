class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        sur_fix = [0] * (len(nums)+1)
        res = 0
        for i in range(len(nums)-1, -1, -1):
            sur_fix[i] = (nums[i] | sur_fix[i+1])
        
        pre_fix = 0
        for i in range(len(nums)):
            tmp = pre_fix|(nums[i]*pow(2,k))|sur_fix[i+1]
            res = max(res, tmp)
            pre_fix |= nums[i]            
        return res
            
