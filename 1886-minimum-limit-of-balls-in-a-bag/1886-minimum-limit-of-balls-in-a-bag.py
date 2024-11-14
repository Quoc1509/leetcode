class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, max(nums)
        def check(mid):
            count = 0
            for num in nums:
                count += ceil(num / mid)-1
            return count > maxOperations
        while l <= r:
            m = (l+r)//2
            if check(m):
                l = m + 1
            else:
                r = m - 1
        return l

