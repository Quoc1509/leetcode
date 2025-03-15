class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l, r = min(nums), max(nums)
        def check(mid):
            i, count = 0, 0
            while i < len(nums):
                if nums[i] <= mid:
                    count += 1
                    if count == k: return True
                    i += 1
                i += 1 
            return False
                
        while l <= r:
            m = (l+r)//2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l