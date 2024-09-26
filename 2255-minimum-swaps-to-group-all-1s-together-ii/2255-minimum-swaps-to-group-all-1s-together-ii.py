class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        one = nums.count(1)
        res = 0
        for i in range(one):
            if nums[i] == 0:
                res += 1
        nums = nums + nums
        l = 0
        temp = res
        for r in range(one, len(nums)):
            if nums[r] == 0:
                temp += 1
            if nums[l] == 0:
                temp -= 1
            l += 1
            res = min(res, temp)
        return res