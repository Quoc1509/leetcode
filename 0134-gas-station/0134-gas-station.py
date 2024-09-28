class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ind = 0
        cur = 0
        total = 0
        temp = [a-b for a, b in zip(gas, cost)]
        print(temp)
        for i, e in enumerate(temp):
            cur += e
            if cur < 0:
                ind = i + 1
                total += cur
                cur = 0
                
        return ind if cur + total >= 0 else -1
