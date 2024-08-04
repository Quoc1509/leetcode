class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        temp = []
        for i in range(len(nums)):
            cur = nums[i]
            temp.append(cur)
            for j in range(i+1, len(nums)):
                cur += nums[j] 
                temp.append(cur)
        temp.sort()

        res = 0
        for i in range(left-1, right):
            res += temp[i]
        return res % (10**9+7)