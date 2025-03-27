class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        count = [0] * numCourses
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
            count[a] += 1
        q = deque()
        for i, num in enumerate(count):
            if num == 0:
                q.append(i)
        
        res = []
        while q:
            for _ in range(len(q)):
                course = q.popleft()
                res.append(course)
                for next_course in graph[course]:
                    count[next_course] -= 1
                    if count[next_course] == 0:
                        q.append(next_course)
        return res if len(res) == numCourses else []