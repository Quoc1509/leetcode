class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        course = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            course[a] += 1
        q = deque()
        for i in range(len(course)):
            if course[i] == 0:
                q.append(i)

        res = []
        while q:
            for _ in range(len(q)):
                n = q.popleft()
                if course[n] == 0:
                    res.append(n)
                for node in graph[n]:
                    course[node] -= 1
                    if course[node] == 0:
                        q.append(node)
                        
        return True if len(res) == numCourses else False
