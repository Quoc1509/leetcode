class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # gas = 0
        # for n in nums:
        #     if gas < 0:
        #         return False
        #     elif n > gas:
        #         gas = n
        #     gas -= 1
            
        # return True
        j, res = 0, 0
        for i in range(len(nums)):
            if i > j:
                return False
            if j < i+nums[i]:
                j = i + nums[i]
                res += 1
            if j >= len(nums)-1:
                return True
        return False
        
        