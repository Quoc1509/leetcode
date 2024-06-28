class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events, key = lambda x: x[0])
        heap = []
        d, res, i = 1, 0, 0
        while d <= 100000 and (heap or i < len(events)):
            while i < len(events) and events[i][0] <= d:
                # temp = [events[i][1], events[i][0]]
                heapq.heappush(heap, events[i][1])
                i += 1
            while heap and d > heap[0]:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                res += 1
            d +=  1
        return res 
