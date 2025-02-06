class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        pre = defaultdict(int)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                pre[nums[i]*nums[j]] += 1
        res = 0
        for val in pre.values():
            while val > 1:
                res += ((val-1) * (2**3))
                val -= 1
        return res
