class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l, r = 0, max(nums)

        def check(m):
            count, i = 0, 0

            while i < len(nums):
                if nums[i] <= m:
                    count += 1
                    i += 1
                i += 1
            return count >= k

        while l <= r:
            mid = (l+r)//2
            if check(mid):
                r = mid-1
            else:
                l = mid+1
        return l
