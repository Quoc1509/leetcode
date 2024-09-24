class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        diffMP = defaultdict(int)

        for a, b in intervals:
            diffMP[a] += 1
            diffMP[b] -= 1
        arr = sorted([[a, b] for a, b in diffMP.items()])
        print(arr)
        res = arr[0][1]
        for i in range(1, len(arr)):
            arr[i][1] = arr[i-1][1] + arr[i][1]
            res = max(arr[i][1], res)
         
        return res