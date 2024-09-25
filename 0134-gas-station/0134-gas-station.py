class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur = 0
        total = 0
        res = 0
        for i in range(len(gas)):
            cur += gas[i] - cost[i]    
            if cur < 0:
                total += cur
                cur = 0
                res = i+1
            
        return res if cur + total >= 0 else -1