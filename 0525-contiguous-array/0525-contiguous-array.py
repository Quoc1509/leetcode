class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        one = zero = 0
        prefix = {0:-1}
        res = 0
        for i in range(len(nums)):
            if nums[i]:
                one += 1
            else:
                zero += 1
            num = zero - one
            if num in prefix:
                res = max(res, i-prefix[num])
            else:
                prefix[num] = i
        return res
