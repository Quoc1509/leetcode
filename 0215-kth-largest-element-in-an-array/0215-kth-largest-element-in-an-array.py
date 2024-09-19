class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1: return nums[0]
        def check(mid):
            count = 0
            for i in nums:
                if i >= mid:
                    count += 1
            return count >= k

        l, r = min(nums), max(nums)
        while l <= r:
            m = (r+l)//2
            if check(m):
                l = m + 1
            else:
                r = m -1
        return r