class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        temp = []
        for i in timePoints:
            if i[:2] == "00":
                temp.append(24*60 + int(i[3:]))
                temp.append(int(i[3:]))
                continue
            hour = int(i[:2])
            minute = int(i[3:])
            temp.append(hour*60+minute)
        
        temp.sort()
        res = inf
        for i in range(1, len(temp)):
            res = min(res, temp[i]-temp[i-1])
            if res == 0: return 0
        if temp[-1] - temp[0] != 1440:
            res = min(res, abs(24*60-temp[-1])+temp[0])
        return res
