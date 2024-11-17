class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        res = 1
        for num in nums:
            res -= 1
            if res < 0:
                return False
            res = max(res, num) 
                        
        return True