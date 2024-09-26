class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        total = 0
        for i in nums:
            total += i
            res += prefix[total%k]
            prefix[total%k] += 1
        return res