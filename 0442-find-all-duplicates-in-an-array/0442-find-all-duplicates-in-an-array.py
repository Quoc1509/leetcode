class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # res = []
        # num = 0
        # for i in nums:
        #     if (1<<i) & num:
        #         res.append(i)
        #     else:
        #         num |= (1<<i)
        # return res
        res = []
        for i, e in enumerate(nums):
            d = abs(e)
            if nums[d-1] < 0:
                res.append(d)
            nums[d-1] *= -1
        return res