class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        if len(nums) == 1: return nums[0]
        if nums[l] != nums[l+1]: return nums[l]
        if nums[r] != nums[r-1]: return nums[r]
        
        while l <= r:
            m = (l+r)//2
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            if nums[m] == nums[m-1]:
                if m % 2 == 1:
                    l = m +1
                else:
                    r = m -1
            else:
                if m % 2 == 0:
                    l = m +1
                else:
                    r = m -1
        return -1
