class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l , r = 1, max(nums)

        def check(mid):
            count = 0
            for num in nums:
                count += (num-1)//mid
            return count <= maxOperations

        while l <= r:
            m = (l+r)//2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l

