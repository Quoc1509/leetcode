class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        one = 0
        for i in nums:
            if i == 1:
                one += 1
        res = 0
        for i in range(-one, 0):
            if nums[i] == 0:
                res += 1
        l = -one
        zero = res
        for r in range(len(nums)):
            if nums[l] == 0:
                zero -= 1
            l += 1

            if nums[r] == 0:
                zero += 1
            res = min(zero, res)
        return res
