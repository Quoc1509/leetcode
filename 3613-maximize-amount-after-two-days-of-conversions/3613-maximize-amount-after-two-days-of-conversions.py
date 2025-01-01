class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        def create_map(arr1, arr2):
            mp = defaultdict(list)

            for i in range(len(arr1)):
                a, b = arr1[i]
                mp[a].append((b, arr2[i]))
                mp[b].append((a, 1/arr2[i]))
            return mp

        def convert(mon, typ, mp):
            temp = deque()
            que = deque()
            que.append((mon, typ))
            visit = set()
            visit.add(typ)
            while que:
                for _ in range(len(que)):
                    rank, node = que.popleft()
                    temp.append((rank, node))
                    for a, b in mp[node]:
                        if a not in visit:
                            que.append((rank*b, a))
                            visit.add(a)
            return temp

        def check(arr):
            ans = 1
            for a, b in arr:
                if b == initialCurrency:
                    ans = max(ans, a)
            return ans
        mp1 = create_map(pairs1, rates1)
        mp2 = create_map(pairs2, rates2)


        arr = convert(1, initialCurrency, mp1)
        res = check(arr)
        for r, t in arr:
            arr = convert(r, t, mp2)
            res = max(res, check(arr))

        return res