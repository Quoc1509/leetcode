class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        monoStack = []
        for num in arr:
            maxNum = num
            while monoStack and monoStack[-1] > num:
                maxNum = max(maxNum, monoStack.pop())
            monoStack.append(maxNum) 
        return len(monoStack)