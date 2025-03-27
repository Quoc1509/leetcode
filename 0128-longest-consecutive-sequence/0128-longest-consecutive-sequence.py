class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp = set(nums)
        res = 0
        for num in nums:
            count = 1
            n = num
            while n-1 in temp:
                count +=1
                temp.remove(n-1)
                n -= 1
            n = num
            while n+1 in temp:
                count += 1
                temp.remove(n+1)
                n += 1
            res = max(res, count)
        return res