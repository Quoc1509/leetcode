class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)-1):
            tmp = upper - nums[i]
            # l, r = i+1, len(nums)-1
            # while l <= r:
            #     m = (l + r)//2
            #     if tmp >= nums[m]:
            #         l = m + 1
            #     else: 
            #         r = m - 1
            # hi = r
            # tmp = lower - nums[i]
            # l, r = i + 1, len(nums)-1
            # while l <= r:
            #     m = (l+r)//2
            #     if tmp <= nums[m]:
            #         r = m - 1
            #     else:
            #         l = m + 1
            r = bisect_right(nums, upper-nums[i], i+1, len(nums))
            l = bisect_left(nums, lower-nums[i], i+1, len(nums))
            res += (r-l)

        return res