class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visit = set()
        res = set()
        temp = deque()
        for r in range(len(s)):
            temp.append(s[r])
            if len(temp) == 10:
                st = ''.join(temp)
                if st in visit:
                    res.add(st)
                else:
                    visit.add(st)
                temp.popleft()
        
        print(res, visit)
        return list(res)
        