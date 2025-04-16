class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        name = defaultdict(str)
        graph = defaultdict(list)
        for s in accounts:
            for i in range(1, len(s)):
                graph[s[i]].append(s[i])
                for j in range(i+1,len(s)):
                    graph[s[i]].append(s[j])
                    graph[s[j]].append(s[i])
                name[s[i]] = s[0]
                
        res = []
        visit = set()

        def bfs(email):
            visit.add(email)
            q = deque([email])
            temp = []
            while q:
                for _ in range(len(q)):
                    e = q.popleft()
                    temp.append(e)
                    for ne in graph[e]:
                        if ne not in visit:
                            q.append(ne)
                            visit.add(ne)
            return temp

        for key in graph.keys():
            if key not in visit:
                temp = bfs(key)
                temp.sort()
                res.append([name[key]])
                res[-1].extend(temp)
            
        return res