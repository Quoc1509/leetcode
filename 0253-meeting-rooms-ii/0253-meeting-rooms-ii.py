class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        length = 0
        for a, b in intervals:
            length = max(length, b)
        diffArr = [0] * (length+1)

        for a, b in intervals:
            diffArr[a] += 1
            diffArr[b] -= 1
        res = diffArr[0]
        for i in range(1, len(diffArr)):
            diffArr[i] = diffArr[i-1] + diffArr[i]
            res = max(diffArr[i], res)
         
        return res