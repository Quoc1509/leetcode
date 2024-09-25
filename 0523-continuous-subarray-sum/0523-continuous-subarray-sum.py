class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = {0:-1}
        total = 0
        for i, e in enumerate(nums):
            total += nums[i]
            
            remain = total % k
            
            if remain in mp:
                if i - mp[remain] >= 2:
                    return True
            else:
                mp[remain] = i
        return False
            
            