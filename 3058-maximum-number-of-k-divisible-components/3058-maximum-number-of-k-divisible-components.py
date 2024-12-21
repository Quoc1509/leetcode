class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        mp = defaultdict(list)
        for a, b in edges:
            val =  + values[b]
            mp[a].append(b)
            mp[b].append(a)
        res= [0]
        def dfs(n, pre):
            total = values[n]
            for no in mp[n]:
                if no != pre:
                    a = dfs(no, n)
                    if a % k == 0:
                        res[0] += 1
                    total += a
            return total
        dfs(0, -1)
        return res[0]+1