class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        total, res, duplicate = 0, 0, 0
        
        for i, e in enumerate(nums):
            res ^= (i + 1) ^ e
            if (total & (1 << e)) != 0:  
                duplicate = e 
            total |= (1 << e)  

        return [duplicate, res ^ duplicate]
