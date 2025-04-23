class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        maxNum = 0
        minNum = 0
        cur = 0

        for num in differences:
            cur = num + cur
            maxNum = max(maxNum, cur)
            minNum = min(minNum, cur)
            
        dif = maxNum - minNum 

        return max(0, (upper - lower) - (maxNum - minNum) + 1)
        