class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        pair, res, l = 0, 0, 0
        for r in range(len(nums)):
            pair += count[nums[r]]
            count[nums[r]] += 1
            
            while pair >= k:
                res += len(nums)-r
                count[nums[l]] -= 1
                pair -= count[nums[l]]
                l += 1
        return res