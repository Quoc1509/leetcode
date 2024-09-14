class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        maxNum, preNum = 0, 0
        N = len(nums)
        i = 0
        while i < N:
            if nums[i] >= maxNum:
                preNum = maxNum
                maxNum = nums[i]
                count = 0
                while i < N and nums[i] == maxNum:
                    count += 1
                    i += 1
                i -= 1
                if preNum == maxNum:
                    res = max(res, count)
                else:
                    res = count
            i += 1

        return res
