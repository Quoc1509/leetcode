class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        

        def backTracking(st):
            if st == '':
                return ['']
            res = []
            for i in wordDict:
                l = len(i)
                temp = st[:l]
                if i == temp:
                    ans = backTracking(st[l:])
                    if ans is not None:
                        for j in range(len(ans)):
                            if len(ans[j]) == 0:
                                ans[j] = i
                            else:
                                ans[j] = i + " " + ans[j]
                        # print(st, i, ans)
                        res.extend(ans)
                        
                    
            if res:
                return res
            return None
        return backTracking(s)

                