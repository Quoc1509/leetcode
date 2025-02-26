class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res1 = 0
        temp = 0
        for num in nums:
            if temp + num < 0:
                temp = 0
            else:
                temp += num
                res1 = max(res1, temp)
        res2 = 0
        temp = 0
        for num in nums:
            if temp+num > 0:
                temp = 0
            else:
                temp += num
                res2 = min(res2, temp)

        return max(res1, abs(res2))