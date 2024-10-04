class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        hashmap = defaultdict(int)
        total = 0
        for i in range(k):
            hashmap[nums[i]] += 1
            total += nums[i]
        if len(hashmap) == k:
            res = total
        l = 0
        for r in range(k, len(nums)):
            hashmap[nums[r]] += 1
            total += nums[r]
            hashmap[nums[l]] -= 1
            if hashmap[nums[l]] == 0:
                del hashmap[nums[l]]
            total -= nums[l]
            l += 1
            if len(hashmap) == k:
                res = max(res, total)
        return res