class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        count = [0] * numCourses
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
            count[a] += 1
        q = deque()
        for i, num in enumerate(count):
            if num == 0:
                q.append(i)
        
        res = 0
        while q:
            res += len(q)
            for _ in range(len(q)):
                course = q.popleft()
                for next_course in graph[course]:
                    count[next_course] -= 1
                    if count[next_course] == 0:
                        q.append(next_course)
        return res == numCourses