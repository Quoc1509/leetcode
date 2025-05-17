class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        l, r = 0, len(nums)-1
        i = l
        while i <= r:
            while l < r and nums[l] == 0:
                l += 1
            while r > l and nums[r] == 2:
                r -= 1            
            i = max(i, l)
            if i > r:
                break   
            if nums[i] == 1:
                i += 1
            else:
                if nums[i] == 0:
                    nums[i], nums[l] = nums[l], nums[i]
                    l += 1
                elif nums[i] == 2:
                    nums[i], nums[r] = nums[r], nums[i]
                    r -= 1
                