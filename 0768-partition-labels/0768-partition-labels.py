class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        mp = defaultdict(int)
        l, res = 0, 0

        def check():
            for key, item in mp.items():
                
                if count[key] != item:
                    return False
            return True
        res = []
        for r in range(len(s)):  
            mp[s[r]] += 1
            if check():
                res.append(r-l+1)
                l = r+1
                
        return res
