class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix = [defaultdict(int) for _ in range(len(s)+1)]

        for i in range(len(s)):
            prefix[i+1] = prefix[i].copy()
            prefix[i+1][s[i]] += 1
            
        res = []
        for a, b in queries:
            if a == b:
                res.append(1)
                continue
            
            temp = prefix[b+1].copy()
            count = 0
            for key, item in temp.items():
                temp[key] -= prefix[a][key]
                
                count += ((temp[key]*(temp[key]+1))//2)
            res.append(count)
        return res