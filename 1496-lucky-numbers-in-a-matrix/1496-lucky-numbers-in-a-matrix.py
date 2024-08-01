class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        maxArray = [-inf] * len(matrix[0])
        minArray = [inf] * len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                maxArray[j] = max(matrix[i][j], maxArray[j])
            minArray[i] = min(matrix[i])
        minArray = set(minArray)
        res= []
        for i in maxArray:
            if i in minArray:
                res.append(i)
        return res