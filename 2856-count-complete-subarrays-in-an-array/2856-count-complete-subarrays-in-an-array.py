class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        total = len(set(nums))
        l, res = 0, 0
        for r in range(len(nums)):
            mp[nums[r]] += 1
            while len(mp) == total:
                res += len(nums) - r
                mp[nums[l]] -= 1
                if mp[nums[l]] == 0:
                    del mp[nums[l]]
                l += 1
        return res