class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        combine = list(zip(timestamp, username, website))
        combine.sort()
        mp = defaultdict(list)
        for a, b, c in combine:
            mp[b].append(c)
        count = defaultdict(int)

        def helper(arr):
            N = len(arr)
            seen = set()
            for i in range(N):
                for j in range(i+1, N):
                    for k in range(j+1, N):
                        triplet = (arr[i], arr[j], arr[k])
                        if triplet not in seen:
                            seen.add(triplet)
                            count[triplet] += 1



        for key, item in mp.items():
                helper(item)
        res = []
        view = 0
        for key, item in count.items():
            if item > view:
                view = item
                res = [list(key)]
            elif item == view:
                res.append(list(key))
        res.sort()
        return res[0]
            