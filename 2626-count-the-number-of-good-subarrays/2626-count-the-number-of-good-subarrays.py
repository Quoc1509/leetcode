class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        r, res, pair = 0, 0, 0
        count = defaultdict(int)
        for l in range(len(nums)):
            while r < len(nums) and pair < k:
                count[nums[r]] += 1
                pair += (count[nums[r]] - 1)
                r += 1
            if pair >= k:
                res += (len(nums)-r+1)
            # else: 
            #     break
            count[nums[l]] -= 1
            pair -= count[nums[l]]
        return res
