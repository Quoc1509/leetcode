class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = [0]
        memo = {}
        def BT(total):
            if total == target:
                return 1
            if total > target:return 0
            if total in memo: return memo[total]
            res = 0
            for j in nums:
                temp = BT(total + j)
                res += temp
            memo[total] = res
            return memo[total]
        
        return BT(0)