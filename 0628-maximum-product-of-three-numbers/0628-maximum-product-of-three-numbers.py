class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        maxF = maxS = maxT = -inf
        minF = minS = inf
        for i in nums:
            if i > maxF:
                maxT = maxS
                maxS = maxF
                maxF = i
            elif i > maxS:
                maxT = maxS
                maxS = i
            elif i > maxT:
                maxT = i
            if i < minF:
                minT = minS
                minS = minF
                minF = i
            elif i < minS:
                minT = minS
                minS = i
 
        return max(maxF*maxS*maxT, minF*minS*maxF)