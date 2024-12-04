class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        count = Counter(nums)    
        total = sum(nums)
        nums.sort(reverse=True)
        for num in nums:
            count[num] -= 1
            temp = total - num
            if temp/2 in count and count[temp/2] > 0:
                return num
            count[num] += 1
            