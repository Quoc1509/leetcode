class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        extra = target // total
        target %= total
        res = inf
        N, l = 0, 0
        newNums = nums+nums
        for r in range(len(newNums)):
            N += newNums[r]
            while N > target:
                N -= newNums[l]
                l += 1
            if N == target:
                res = min(res, r-l+1)
        return -1 if res == inf else extra*len(nums) + res

