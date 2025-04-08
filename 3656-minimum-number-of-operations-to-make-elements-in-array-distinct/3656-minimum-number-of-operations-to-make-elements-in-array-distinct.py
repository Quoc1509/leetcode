class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for i in range(len(nums)):
            if len(count) == len(nums)-i:
                break
            if i % 3 == 0:
                res += 1
            count[nums[i]] -= 1
            if count[nums[i]] == 0:
                del count[nums[i]]
        return res
