class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        name = {}
        graph = defaultdict(list)
        for s in accounts:
            n = s[0]
            f_email = s[1]
            for email in s[1:]:
                name[email] = n
                graph[f_email].append(email)
                graph[email].append(f_email)
                
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
                res.append([name[key]]+sorted(temp))

            
        return res