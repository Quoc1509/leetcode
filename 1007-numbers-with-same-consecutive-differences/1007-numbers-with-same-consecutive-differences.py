class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        def dfs(num):
            if len(num) == n and num[0] != '0':
                res.append(int(num))
                return
            if len(num) > n: return
            for i in range(10):
                if len(num) == 0 or abs(int(num[-1]) - i) == k:
                    dfs(num+str(i))
        
        # for i in range(10):
        #     dfs(str(i))
        dfs('')

        return res
            