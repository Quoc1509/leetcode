class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        count = Counter(nums)    
        total = sum(nums)
        res = -inf
        for num in nums:
            count[num] -= 1
            temp = total - num
            if temp/2 in count and count[temp/2] > 0:
                res = max(res, num)
            count[num] += 1
        return res
            