class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # hashMap = defaultdict(int)
        # for a, b in intervals:
        #     hashMap[a] += +1
        #     hashMap[b+1] += -1
        # count = [[a, b] for a, b in hashMap.items()]
        # count.sort()
        # res = count[0][1]
        # for i in range(1, len(count)):
        #     count[i][1] += count[i-1][1]
        #     res = max(res, count[i][1])
        # return res
        intervals.sort()
        heap = []
        for start, end in intervals:
            
            if heap and heap[0] < start:
                heappop(heap)
            heappush(heap, end)

            
        return len(heap)