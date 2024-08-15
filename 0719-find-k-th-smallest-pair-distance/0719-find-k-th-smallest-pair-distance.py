class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        l, r = 0, max(nums)-min(nums)

        def check(mid):
            l, pair = 0, 0
            for r in range(len(nums)):
                while nums[r]-nums[l] > mid:
                    l += 1
                pair += (r-l)
            
            return pair >= k


        while l <= r:
            m = (l+r)//2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l
