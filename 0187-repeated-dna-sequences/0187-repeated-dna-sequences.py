class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visit = set()
        res = set()
        for i in range(len(s)-9):
            temp = s[i:i+10]
            if temp in visit:
                res.add(temp)
            else:
                visit.add(temp)
        print(res, visit)
        return list(res)
        