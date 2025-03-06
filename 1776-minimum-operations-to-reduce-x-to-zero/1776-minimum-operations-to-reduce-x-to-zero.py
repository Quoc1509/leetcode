class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        temp = nums + nums
        total, l, res = 0, 0, inf
        for r in range(len(temp)):
            total += temp[r]
            while total > x:
                total -= temp[l]
                l += 1
            if total == x:
                if (l == 0 or l <= len(nums)-1 <= r) and r-l < len(nums):
                    res = min(res, r-l+1)
        return res if res != inf else -1