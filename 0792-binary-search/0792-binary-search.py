class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) <= 0:
            return -1
        l = 0
        r = len(nums)-1
        while l <= r:
            
            m = (l+r+1)//2
            print(l,r,m)
            if nums[m] > target:
                r = m -1
            else:
                l = m + 1
        print(r)
        if nums[r] == target:
            return r
        return -1