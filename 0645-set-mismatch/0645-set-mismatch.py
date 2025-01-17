class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = 0
        for i, e in enumerate(nums):
            res ^= (i + 1) ^ e

        bit = res&(-res) # tim bit 1 dau tien cua mot so
        num = 0
        for i, e in enumerate(nums):
            if (i + 1) & bit:
                num ^= (i + 1)
            if e & bit:
                num ^= e

        for n in nums:
            if num == n:
                return [num, res^num]
        return [res^num, num]
