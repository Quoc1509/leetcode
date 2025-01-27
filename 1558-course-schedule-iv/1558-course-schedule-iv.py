class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        S = {}
        def dfs(i):
            if i not in S:
                temp = set()
                temp.add(i)
                for n in graph[i]:
                    temp |= dfs(n)
                S[i] = temp
            return S[i]

        for i in range(numCourses):
            dfs(i)
        res = []
        for a, b in queries:
            res.append(b in S[a])
        return res
        
        


        