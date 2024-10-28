class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        res = 1
        s = set(nums)
        for num in nums:
            count = 1
            temp = num * num
            while temp in s:
                count += 1
                s.remove(temp)
                temp *= temp

            temp = sqrt(num)
            while temp in s:
                count += 1
                s.remove(temp)
                temp = sqrt(temp)
            res = max(res, count)
        return res if res > 1 else -1

