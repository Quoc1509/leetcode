class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        extra = 0
        o, c = 0, 0
        for i in s:
            if i == '(':
                o += 1
            elif i == ')':
                o -= 1          
            if o < 0:
                extra += abs(o)
                o = 0
        extra += o
        res = []
        def dfs(path, index, pair, k):
            if index == len(s): 
                if pair == 0 and k == 0:
                    res.append(path[:])
                return
            if k < 0 or pair < 0:
                return
            if s[index] != '(' and s[index] != ')':
                dfs(path + s[index], index+1, pair, k)
                return
            j = index
            while j < len(s) and s[index] == s[j]:
                j += 1
            for h in range(min(k, j-index) + 1):
                a = j-index-h
                npair = pair + (a if s[index] == '(' else -a)
                dfs(path + s[index:index+a], j, npair, k-h)
        dfs('', 0, 0, extra)      
        return res if res else [""]