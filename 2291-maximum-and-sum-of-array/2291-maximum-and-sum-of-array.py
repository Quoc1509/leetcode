class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        
        @cache
        def dfs(i, slot):
            if i >= len(nums):
                return 0
            temp = 0
            for s in range(1, numSlots+1):
                if (slot >> (2*(s-1))) & 2 >= 2:
                    continue
                new_slot = slot + ( 1 << (2*(s-1)))
                temp = max(temp, dfs(i+1, new_slot)+(nums[i]&s))
                
            return temp
        return dfs(0, 0)
                