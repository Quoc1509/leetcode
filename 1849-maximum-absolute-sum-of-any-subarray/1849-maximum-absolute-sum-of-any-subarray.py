class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res1 = res2 = 0
        temp1 = temp2 = 0
        for num in nums:
            if temp1 + num < 0:
                temp1 = 0
            else:
                temp1 += num
                res1 = max(res1, temp1)
            if temp2+num > 0:
                temp2 = 0
            else:
                temp2 += num
                res2 = min(res2, temp2)

        return max(res1, abs(res2))