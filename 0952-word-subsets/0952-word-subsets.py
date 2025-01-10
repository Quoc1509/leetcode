class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        mp = defaultdict(int)
        for word in words2:
            count = Counter(word)
            for k, e in count.items():
                mp[k] = max(mp[k], e)

        def check(c):
            for k, e in mp.items():
                if c[k] < e:
                    return False
            return True

        res = []
        for word in words1:
            count = Counter(word)
            c = check(count)
            if c:
                res.append(word)
        return res