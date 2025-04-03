class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        l, res = 0, 0
        d = 0
        for r in range(len(nums)):
            if nums[r] % 2 != 0:
                count += 1
                d = 0
            while count >= k:
                if count == k:
                    d += 1
                if nums[l] %2 != 0:
                    count -= 1
                l += 1
            res += d
        return res