class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]: return nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            
            m = (l+r)//2
            if nums[m] > nums[-1]:
                l = m + 1
            else:
                r = m - 1   
            
        return nums[l]