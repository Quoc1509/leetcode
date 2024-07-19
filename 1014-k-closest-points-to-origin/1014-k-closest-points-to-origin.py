class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for x, y in points:
            dis = math.sqrt(x*x+y*y)
            if len(res) < k:
                heapq.heappush(res, (-dis, (x, y)))
                
            else:
                if -dis > res[0][0]:
                    heapq.heappop(res)
                    heapq.heappush(res, (-dis, (x, y)))
        heap = []
        for i, j in res:
            heap.append(j)
        return heap
                     

        