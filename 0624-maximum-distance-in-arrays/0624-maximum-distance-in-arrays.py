class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res, numMin, numMax = 0, arrays[0][0], arrays[0][-1]
        for i in range(1, len(arrays)):
            tempMin, tempMax = arrays[i][0], arrays[i][-1]
            dif1 = abs(tempMax-numMin)
            dif2 = abs(tempMin-numMax)
            res = max(res, dif1, dif2)
            numMin = min(numMin, tempMin)
            numMax = max(numMax, tempMax)
        return res