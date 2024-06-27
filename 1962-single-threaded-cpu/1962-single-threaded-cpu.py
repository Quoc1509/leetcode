class Solution:
    def getOrder(self, tasks: List[List[int]]) -> int:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks = sorted(tasks, key=lambda x: x[0])

        endTime = tasks[0][0]
        i = 0
        heap,res = [], []
        while heap or i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= endTime:
                temp = [tasks[i][1], tasks[i][2]]
                tasks[i].append(temp)
                
                heapq.heappush(heap, temp)
                i += 1
            if heap:
                temp = heapq.heappop(heap)
                endTime += temp[0]
                res.append(temp[1])
            else:
                endTime = tasks[i][0]

        return res