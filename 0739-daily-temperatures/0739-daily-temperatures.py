class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monoStack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while monoStack and temperatures[monoStack[-1]] < temperatures[i]:
                idx = monoStack.pop()
                res[idx] = i-idx
            monoStack.append(i)        
        return res