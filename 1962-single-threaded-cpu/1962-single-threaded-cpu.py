class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        end = tasks[0][0]
        heap, res = [], []
        i = 0
        while heap or i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= end:
                heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            if heap:
                process, idx = heappop(heap)
                res.append(idx)
                end += process
            else:
                heappush(heap, (tasks[i][1], tasks[i][2]))
                end = tasks[i][0]
                i += 1
        return res