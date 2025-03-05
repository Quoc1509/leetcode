class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        graph = defaultdict(list)
        for a, b in synonyms:
            graph[a].append(b)
            graph[b].append(a)
        
        res = []
        q = deque()
        q.append(text)
        visit = set()
        visit.add(text)
        while q:
            for _ in range(len(q)):
                s = q.popleft()
                res.append(s)
                arr = s.split()
                for i, e in enumerate(arr):
                    for w in graph[e]:
                        arr[i] = w
                        temp = ' '.join(arr)
                        if temp not in visit:
                            q.append(temp)
                            visit.add(temp)
        return sorted(res)
                                
            