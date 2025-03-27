class Solution:
    def jump(self, nums: List[int]) -> int:
        # if len(nums) == 1: return 0
        ne_i = 0
        j = 0
        res = 0
        for i in range(len(nums)):
            j = max(j, nums[i]+i)
            if i == ne_i:
                res += 1
                ne_i = min(len(nums)-1, j)
        return res-1