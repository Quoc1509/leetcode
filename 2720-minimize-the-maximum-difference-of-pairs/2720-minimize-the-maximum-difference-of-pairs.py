class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()
        
        def check(mid):
            count = 0
            i = 0
            while i < len(nums)-1:
                if nums[i+1]-nums[i] <= mid:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p
        l, r = 0, nums[-1]
        while l <= r:
            m = (l+r)//2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l
